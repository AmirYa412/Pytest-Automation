from typing import List, Dict, Any, Optional
from unit_tests.src.google.google_auth import GoogleClient
import requests
from unit_tests.src.exceptions.google_exceptions import GooglePhotosFetchError, PaginationError


class GoogleClientPhotos(GoogleClient):
    """Google Photos API client with pagination and data enrichment."""

    DEFAULT_PAGE_SIZE = 10
    MAX_PAGE_SIZE = 100

    def get_user_google_photos(self, enrich: bool = True) -> List[Dict[str, Any]]:
        """Get all user's Google photos."""

        try:
            user_data = self.fetch_user_data_from_google()
            user_photos = user_data["media"]["photos"]

            if enrich and len(user_photos) > 0:
                user_photos = self._enrich_photos(user_photos)

            return user_photos

        except KeyError as e:
            raise GooglePhotosFetchError(f"Invalid photos data structure: {str(e)}") from e
        except Exception as e:
            raise GooglePhotosFetchError(f"Could not fetch photos data from Google: {str(e)}") from e

    def get_photos_paginated(self, page: int = 1,page_size: int = DEFAULT_PAGE_SIZE) -> Dict[str, Any]:
        """Get user's photos with pagination support."""

        # Validate pagination parameters
        if page < 1:
            raise PaginationError(f"Page number must be >= 1, got {page}")

        if page_size < 1 or page_size > self.MAX_PAGE_SIZE:
            raise PaginationError(
                f"Page size must be between 1 and {self.MAX_PAGE_SIZE}, got {page_size}"
            )

        try:
            all_photos = self.get_user_google_photos(enrich=True)

            total_photos = len(all_photos)
            total_pages = (total_photos + page_size - 1) // page_size  # Ceiling division

            if page > total_pages and total_photos > 0:
                raise PaginationError(
                    f"Page {page} exceeds total pages {total_pages}"
                )

            start_idx = (page - 1) * page_size
            end_idx = start_idx + page_size

            photos_page = all_photos[start_idx:end_idx]

            return {
                "photos": photos_page,
                "page": page,
                "page_size": page_size,
                "total_photos": total_photos,
                "total_pages": total_pages,
                "has_next": page < total_pages,
                "has_prev": page > 1
            }

        except PaginationError:
            raise
        except Exception as e:
            raise PaginationError(f"Pagination failed: {str(e)}") from e

    def get_all_photos_paginated(self, page_size: int = DEFAULT_PAGE_SIZE, max_pages: Optional[int] = None) -> List[Dict[str, Any]]:
        """Fetch all photos across multiple pages."""

        all_photos = []
        page = 1

        try:
            while True:
                if max_pages and page > max_pages:
                    break

                result = self.get_photos_paginated(page=page, page_size=page_size)
                all_photos.extend(result["photos"])

                if not result["has_next"]:
                    break

                page += 1

            return all_photos

        except Exception as e:
            raise PaginationError(f"Failed to fetch all pages: {str(e)}") from e

    @staticmethod
    def _enrich_photos(photos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Enrich photo data with additional metadata."""
        for photo in photos:
            photo["service"] = "google_photos"

            # Add computed fields
            if "img_id" in photo:
                photo["display_id"] = f"PHOTO_{photo['img_id']}"

            if "link" in photo:
                photo["thumbnail"] = f"{photo['link']}/thumbnail"

        return photos

    def fetch_photos_with_query_params(self, page: int = 1, page_size: int = DEFAULT_PAGE_SIZE, sort_by: str = "created_at",
            order: str = "desc") -> Dict[str, Any]:
        """Fetch photos with custom query parameters."""

        try:
            self._ensure_authenticated()

            params = {
                "page": page,
                "page_size": page_size,
                "sort_by": sort_by,
                "order": order
            }

            response = self.session.get(
                f"{self.BASE_URL}/google/photos",
                headers=self._get_headers(),
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:
            raise GooglePhotosFetchError(f"Failed to fetch photos with params: {str(e)}") from e
