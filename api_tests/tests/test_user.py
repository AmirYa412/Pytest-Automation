from api_tests.support.environment import Environment
from pytest import mark
from api_tests.api_models.user import User
from datetime import datetime, timezone

pytestmark = [mark.api, mark.user]


@mark.usefixtures("api_test_class_setup")
class TestUserLogin:

    client: User
    env : Environment

    def setup_method(self):
        if not hasattr(self.__class__, 'client'):
            self.__class__.client = User(self.env)

    def teardown_method(self):
        self.client.reset_session()

    def test_user_login_success(self):
        user = self.env.users["user_1"]
        response = self.client.login_user(username=user["name"], password=user["password"])
        assert response.status_code == 200
        response_data = response.json()
        self.client.validate_login_response_schema(response_data)  # ✅ Add this

        time_format = "%a %b %d %H:%M:%S UTC %Y"
        expires_time = datetime.strptime(response.headers["x-expires-after"], time_format).replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        assert expires_time > now, "Token expiration time is not in the future"

        assert response_data["code"] == 200
        assert "logged in user session:" in response_data["message"] is not None
        assert response_data["message"].split(":")[1].isnumeric(), f"session id is wrong: {response_data['message']}"

