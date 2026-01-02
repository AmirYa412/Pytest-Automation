import pytest
import requests
import responses
from datetime import datetime, timedelta
from unit_tests.src.google.google_auth import GoogleClient
from unit_tests.src.exceptions.google_exceptions import GoogleAuthError
from unit_tests.utils.mocks.google_mocks import GoogleAuthMocks



class TestGoogleClientAuthentication:

    @responses.activate
    def test_login_success(self):
        mock_response = GoogleAuthMocks.successful_login_response()
        responses.add(
            responses.POST,
            "https://dev.google.com/api/auth",
            json=mock_response,
            status=200
        )

        client = GoogleClient("user@test.com", "password123")
        result = client.login()

        assert result["token"] == mock_response["token"]
        assert result["expires_in"] == 3600
        assert client.token == mock_response["token"]
        assert client.token_expiry is not None
        assert client.token_expiry > datetime.now()

    @responses.activate
    def test_login_with_invalid_credentials_raises_error(self):
        responses.add(
            responses.POST,
            "https://dev.google.com/api/auth",
            json=GoogleAuthMocks.invalid_credentials_response(),
            status=401
        )

        client = GoogleClient("wrong@test.com", "wrongpass")
        with pytest.raises(GoogleAuthError) as exc_info:
            client.login()

        assert "Authentication failed: 401" in str(exc_info.value)

    def test_get_headers_with_token_returns_bearer_token(self):
        client = GoogleClient("user@test.com", "password")
        client.token = "test_token_12345"
        headers = client._get_headers()

        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer test_token_12345"
        assert headers["Content-Type"] == "application/json"

    @responses.activate
    def test_login_timeout_raises_error(self):
        responses.add(
            responses.POST,
            "https://dev.google.com/api/auth",
            body=requests.exceptions.Timeout()
        )
        client = GoogleClient("user@test.com", "password")
        with pytest.raises(GoogleAuthError) as exc_info:
            client.login()


    def test_ensure_authenticated_refreshes_expired_token(self, mocker):
        client = GoogleClient("user@test.com", "password")
        client.token = "old_token"
        client.token_expiry = datetime.now() - timedelta(hours=1)
        mock_login = mocker.patch.object(client, 'login')
        client._ensure_authenticated()
        mock_login.assert_called_once()