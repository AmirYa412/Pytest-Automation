from pytest import mark
from api_tests.api_models.user import User
from datetime import datetime, timedelta

@mark.usefixtures("api_test_class_setup")
class TestUserLogin:
    client: User

    def setup_method(self):
        if not hasattr(self.__class__, 'client'):
            self.__class__.client = User(self.env)

    def teardown_method(self):
        self.client.reset_session()

    def test_user_login_success(self):
        user = self.env.users["user_1"]
        response = self.client.login_user(username=user["name"], password=user["password"])
        assert response.status_code == 200

        expires_time = datetime.strptime(response.headers["x-expires-after"], "%a %b %d %H:%M:%S UTC %Y")
        now = datetime.utcnow()
        assert expires_time > now, "Token expiration time is not in the future"

        response_data = response.json()
        assert response_data["code"] == 200
        assert "message" in response_data
        assert "logged in user session:" in response_data["message"] is not None
        assert response_data["message"].split(":")[1].isnumeric(), f"session id is wrong: {response_data['message']}"

