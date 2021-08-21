import pytest
from unit_tests.models.google.google_photos import GooglePhotos
from unit_tests.utils.mocks import GooglePhotosMock

pytestmark = pytest.mark.unit


class TestGooglePhotos:
    def test_get_user_photos(self, mocker):
        mocked_data = GooglePhotosMock.mocked_user_data
        mocker.patch('unit_tests.models.google.google_auth.Google.fetch_user_data_from_google', return_value=mocked_data)
        user_photos = GooglePhotos(user="dummy", password="1234").get_user_google_photos()
        assert user_photos[0]["service"] == "google_photos"
        assert len(user_photos) > 0

    def test_get_first_photo_data(self, mocker):
        mock_gphotos = mocker.MagicMock(name="GooglePhotos.fetch_user_data_from_google")
        mock_gphotos.return_value = {
            "media": {
                "photos": [{"img_id": 111, "link": "dummy.com"}, {"img_id": 222, "link": "dummy.com"}]
            }
        }
        mocker.patch("unit_tests.models.google.google_auth.Google.fetch_user_data_from_google", new=mock_gphotos)
        user_photos = GooglePhotos(user="dummy", password="1234").get_user_google_photos()
        assert user_photos[0]["img_id"] == 111
        assert user_photos[1]["img_id"] == 222


