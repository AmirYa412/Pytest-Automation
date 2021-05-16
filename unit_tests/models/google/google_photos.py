import requests


class GooglePhotos:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def get_user_google_photos(self):  # In our test we will mock this function's return value to avoid Google login
        data = {
            "username": self.user,
            "password": self.user
        }
        session = requests.Session()
        response = session.post("https://www.google.com/api/auth", data=data)
        assert response.status_code == 200
        response = requests.get("https://www.google.com/api/google/photos")
        return response.json()
