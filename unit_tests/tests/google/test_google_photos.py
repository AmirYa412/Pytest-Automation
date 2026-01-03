import pytest
from unit_tests.src.google.google_photos import GoogleClientPhotos
from unit_tests.utils.mocks.google_mocks import GooglePhotosMocks
from unit_tests.src.exceptions.google_exceptions import PaginationError
pytestmark = pytest.mark.unit


class TestGoogleClientPhotos:

    def test_get_user_photos_with_mocked_method(self, mocker):
        mock_data = GooglePhotosMocks.user_data_response(photo_count=5)
        client = GoogleClientPhotos("user@test.com", "password")
        mocker.patch.object(client, 'fetch_user_data_from_google', return_value=mock_data)
        photos = client.get_user_google_photos()

        assert len(photos) == 5
        assert all(photo["service"] == "google_photos" for photo in photos)
        assert all("display_id" in photo for photo in photos)
        assert all("thumbnail" in photo for photo in photos)

    def test_get_user_photos_with_empty_list(self, mocker):
        mock_data = GooglePhotosMocks.empty_photos_response()
        client = GoogleClientPhotos("user@test.com", "password")
        mocker.patch.object(client, 'fetch_user_data_from_google', return_value=mock_data)
        photos = client.get_user_google_photos()

        assert len(photos) == 0
        assert photos == []

    def test_photo_enrichment_adds_metadata(self):
        raw_photos = GooglePhotosMocks.generate_photos_list(count=2)
        client = GoogleClientPhotos("user@test.com", "password")
        enriched = client._enrich_photos(raw_photos)

        for photo in enriched:
            assert photo["service"] == "google_photos"
            assert photo["display_id"] == f"PHOTO_{photo['img_id']}"
            assert photo["thumbnail"] == f"{photo['link']}/thumbnail"

    @pytest.mark.pagination
    @pytest.mark.parametrize("page,page_size,has_next,has_prev", [
        (1, 10, True, False),
        (2, 10, True, True),
        (3, 10, False, True)
    ])
    def test_pagination_navigation_flags(self, mocker, page, page_size, has_next, has_prev):
        mock_data = GooglePhotosMocks.user_data_response(photo_count=25)
        client = GoogleClientPhotos("user@test.com", "password")
        mocker.patch.object(client, 'fetch_user_data_from_google', return_value=mock_data)
        result = client.get_photos_paginated(page=page, page_size=page_size)

        assert result["has_next"] == has_next
        assert result["has_prev"] == has_prev


    @pytest.mark.pagination
    @pytest.mark.parametrize("invalid_page,error_message", [
        (0, "Page number must be >= 1"),
        (-1, "Page number must be >= 1"),
        (-100, "Page number must be >= 1"),
    ])
    def test_pagination_with_invalid_page_number(self, invalid_page, error_message):
        client = GoogleClientPhotos("user@test.com", "password")

        with pytest.raises(PaginationError) as exc_info:
            client.get_photos_paginated(page=invalid_page, page_size=10)

        assert error_message in str(exc_info.value)
