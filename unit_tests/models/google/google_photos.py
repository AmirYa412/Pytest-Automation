import requests


class GooglePhotos:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.session = requests.Session()

    def google_login(self):
        data = {
            "username": self.user,
            "password": self.user
        }
        response = self.session.post("https://www.google.com/api/auth", data=data)
        response.raise_for_status()

    def get_user_google_photos(self):  # In our test we will mock this function's return value to avoid google_login()
        self.google_login()
        response = self.session.get("https://www.google.com/api/google/photos")
        response.raise_for_status()
        return response.json()
