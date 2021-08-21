import requests


class Google:
    """
    Demo class
    """

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.session = requests.Session()

    def login(self):
        try:
            data = {
                "username": self.user,
                "password": self.user
            }
            response = self.session.post("https://dev.google.com/api/auth", data=data)
            return response
        except Exception:
            raise Exception("Could not auth user")

    def fetch_user_data_from_google(self):  # Mocking this function return value
        try:
            response = self.session.get("https://dev.google.com/api/google/photos")
            response.raise_for_status()
            return response.json()
        except Exception:
            raise Exception("Could fetch user's data from Google")
