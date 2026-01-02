import requests
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from unit_tests.src.exceptions.google_exceptions import GoogleAuthError, InvalidResponseError, TokenExpiredError, GooglePhotosFetchError


class GoogleClient:

    BASE_URL = "https://dev.google.com/api"
    DEFAULT_TIMEOUT = 10
    TOKEN_LIFETIME_SECONDS = 3600  # 1 hour

    def __init__(self, user: str, password: str, timeout: int = DEFAULT_TIMEOUT):
        self.user = user
        self.password = password
        self.timeout = timeout
        self.session = self._create_session_with_retries()
        self.token: Optional[str] = None
        self.token_expiry: Optional[datetime] = None

    @staticmethod
    def _create_session_with_retries() -> requests.Session:
        """Create a session with automatic retry configuration."""
        session = requests.Session()

        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE", "HEAD"]
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)

        return session

    def login(self) -> Dict[str, Any]:
        """Authenticate user and obtain access token."""
        try:
            data = {
                "username": self.user,
                "password": self.password
            }

            response = self.session.post(
                f"{self.BASE_URL}/auth",
                json=data,
                timeout=self.timeout
            )
            response.raise_for_status()

            auth_data = response.json()

            # Store token and calculate expiry
            self.token = auth_data.get("token")
            expires_in = auth_data.get("expires_in", self.TOKEN_LIFETIME_SECONDS)
            self.token_expiry = datetime.now() + timedelta(seconds=expires_in)

            return auth_data

        except requests.exceptions.HTTPError as e:
            raise GoogleAuthError(f"Authentication failed: {e.response.status_code}") from e
        except requests.exceptions.Timeout:
            raise GoogleAuthError("Authentication request timed out") from None
        except requests.exceptions.RequestException as e:
            raise GoogleAuthError(f"Authentication request failed: {str(e)}") from e
        except (KeyError, ValueError) as e:
            raise GoogleAuthError(f"Invalid authentication response format: {str(e)}") from e

    def _is_token_expired(self) -> bool:
        """Check if current token is expired."""
        if not self.token or not self.token_expiry:
            return True

        # Add 60 second buffer to refresh before actual expiry
        return datetime.now() >= (self.token_expiry - timedelta(seconds=60))

    def _ensure_authenticated(self) -> None:
        """Ensure valid authentication token exists."""
        if self._is_token_expired():
            self.login()

    def _get_headers(self) -> Dict[str, str]:
        """Get request headers with authentication token."""
        if not self.token:
            raise GoogleAuthError("No authentication token available. Call login() first.")

        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def fetch_user_data_from_google(self) -> Dict[str, Any]:
        """Fetch user data including photos from Google API."""
        try:
            self._ensure_authenticated()

            response = self.session.get(
                f"{self.BASE_URL}/google/photos",
                headers=self._get_headers(),
                timeout=self.timeout
            )
            response.raise_for_status()

            data = response.json()

            # Validate response structure
            if "media" not in data or "photos" not in data["media"]:
                raise InvalidResponseError("Response missing required 'media.photos' structure")

            return data

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise TokenExpiredError("Token expired during request") from e
            raise GooglePhotosFetchError(f"Failed to fetch photos: {e.response.status_code}") from e
        except requests.exceptions.Timeout:
            raise GooglePhotosFetchError("Photos fetch request timed out") from None
        except requests.exceptions.RequestException as e:
            raise GooglePhotosFetchError(f"Photos fetch request failed: {str(e)}") from e
        except (KeyError, ValueError) as e:
            raise InvalidResponseError(f"Invalid response format: {str(e)}") from e