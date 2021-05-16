import pytest
from unit_tests.models.google.google_photos import GooglePhotos
from unit_tests.utils.mocks import GooglePhotosMock

pytestmark = pytest.mark.unit


class TestGooglePhotos:
    def test_get_user_photos(self, mocker):
        user, password = "Amir", "python123"    # In these tests we avoid auth against Google server with mocks
        mocked_data = GooglePhotosMock().mocked_user_items
        mocker.patch('unit_tests.models.google.google_photos.GooglePhotos.get_user_google_photos', return_value=mocked_data)
        user_photos = GooglePhotos(user=user, password=password).get_user_google_photos()
        assert len(user_photos) > 0

    def test_get_first_photo_data(self, mocker):
        mock_gphotos = mocker.MagicMock(name="GooglePhotos.get_user_google_photos")
        mock_gphotos.return_value = [{"img_id": 300, "link": "dummy.com"}, {"img_id": 301, "link": "dummy.com"}]
        mocker.patch("unit_tests.models.google.google_photos.GooglePhotos.get_user_google_photos", new=mock_gphotos)
        user_photos = GooglePhotos(user="dummy", password="1234").get_user_google_photos()
        assert user_photos[0]["img_id"] == 300


