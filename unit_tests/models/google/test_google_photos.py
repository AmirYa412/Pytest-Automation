import pytest
from unit_tests.models.google.google_photos import GooglePhotos
from unit_tests.utils.mocks import GooglePhotosMock

pytestmark = pytest.mark.unit


class TestGooglePhotos:
    def test_get_user_photos(self, mocker):
        user, password = "Amir", "python123"    # In this test we avoid auth against Google server with mocks
        mocked_data = GooglePhotosMock().mocked_user_items
        mocker.patch('unit_tests.models.google.google_photos.GooglePhotos.get_user_google_photos', return_value=mocked_data)
        user_photos = GooglePhotos(user=user, password=password).get_user_google_photos()
        assert len(user_photos) > 0
