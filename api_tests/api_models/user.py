from api_tests.support.client import Client


class User(Client):
    PATH = "/user/login"

    def login_user(self, username, password):
        """Login user with username and password"""
        params = self.get_query_params(username=username, password=password)
        return self.get_request(self.PATH, params=params)

    @staticmethod
    def get_query_params(username=None, password=None):
        return {
            "username": username,
            "password": password
        }


