from jsonschema import validate
from requests import Response
from api_tests.support.client import Client


class User(Client):

    PATH = "/user/login"

    def login_user(self, username: str, password: str) -> Response:
        params = self.get_query_params(username=username, password=password)
        return self.get_request(self.PATH, params=params)

    @staticmethod
    def get_query_params(username: str | None = None, password: str | None = None) -> dict:
        return {
            "username": username,
            "password": password
        }

    @staticmethod
    def validate_login_response_schema(response_data: dict) -> None:
        """Validate user login response structure.

        Args:
            response_data: Login response from API

        Raises:
            ValidationError: If response doesn't match expected schema
        """
        login_schema = {
            "type": "object",
            "properties": {
                "code": {"type": "integer"},
                "type": {"type": "string"},
                "message": {"type": "string"}
            },
            "required": ["code", "type", "message"]
        }
        validate(instance=response_data, schema=login_schema)
