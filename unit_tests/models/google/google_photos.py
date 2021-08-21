from unit_tests.models.google.google_auth import Google


class GooglePhotos(Google):

    def get_user_google_photos(self):
        try:
            user_data = self.fetch_user_data_from_google()
            user_photos = user_data["media"]["photos"]
            if len(user_photos) > 0:
                for item in user_photos:
                    item["service"] = "google_photos"
            return user_photos
        except Exception:
            raise Exception("Could fetch photos's data from Google")

