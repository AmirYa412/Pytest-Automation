import requests


class GooglePhotos:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    @staticmethod
    def get_user_google_photos():  # In our test we will mock this function's return value
        response = requests.get("https://www.google.com/api/auth")
        assert response.status_code == 200
        response = requests.get("https://www.google.com/api/google/photos")
        return response.json()
