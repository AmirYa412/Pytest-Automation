from typing import Dict, List, Any
from datetime import datetime, timedelta


class GoogleAuthMocks:
    """Mock data for authentication scenarios."""

    @staticmethod
    def successful_login_response() -> Dict[str, Any]:
        """Mock successful login response with token."""
        return {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.mock_token",
            "expires_in": 3600,
            "token_type": "Bearer",
            "user_id": "12345"
        }

    @staticmethod
    def expired_token_response() -> Dict[str, Any]:
        """Mock response for expired token."""
        return {
            "token": "expired.token.mock",
            "expires_in": 0,
            "token_type": "Bearer",
            "user_id": "12345"
        }

    @staticmethod
    def invalid_credentials_response() -> Dict[str, str]:
        """Mock error response for invalid credentials."""
        return {
            "error": "invalid_credentials",
            "message": "Username or password is incorrect"
        }


class GooglePhotosMocks:
    """Mock data for Google Photos API responses."""

    @staticmethod
    def generate_photo(photo_id: int) -> Dict[str, Any]:
        """Generate a single mock photo.
        """
        return {
            "img_id": photo_id,
            "link": f"https://photos.google.com/photo/{photo_id}",
            "filename": f"IMG_{photo_id:04d}.jpg",
            "size_bytes": 1024 * 1024 * (photo_id % 5 + 1),  # 1-5 MB
            "created_at": (datetime.now() - timedelta(days=photo_id)).isoformat(),
            "width": 1920,
            "height": 1080
        }

    @staticmethod
    def generate_photos_list(count: int, start_id: int = 1) -> List[Dict[str, Any]]:
        """Generate a list of mock photos."""
        return [
            GooglePhotosMocks.generate_photo(i)
            for i in range(start_id, start_id + count)
        ]

    @staticmethod
    def user_data_response(photo_count: int = 15) -> Dict[str, Any]:
        """Mock complete user data response with photos."""
        return {
            "email": "test.user@gmail.com",
            "username": "Test User",
            "age": 30,
            "user_id": "12345",
            "media": {
                "photos": GooglePhotosMocks.generate_photos_list(photo_count),
                "videos": [],
                "total_storage_mb": photo_count * 2
            }
        }

    @staticmethod
    def paginated_response(
            page: int = 1,
            page_size: int = 10,
            total_photos: int = 25
    ) -> Dict[str, Any]:
        """Mock paginated photos response."""
        total_pages = (total_photos + page_size - 1) // page_size
        start_id = (page - 1) * page_size + 1
        photos_on_page = min(page_size, total_photos - (page - 1) * page_size)

        return {
            "photos": GooglePhotosMocks.generate_photos_list(photos_on_page, start_id),
            "pagination": {
                "page": page,
                "page_size": page_size,
                "total_photos": total_photos,
                "total_pages": total_pages,
                "has_next": page < total_pages,
                "has_prev": page > 1
            }
        }

    @staticmethod
    def empty_photos_response() -> Dict[str, Any]:
        """Mock response with no photos."""
        return {
            "email": "test.user@gmail.com",
            "username": "Test User",
            "media": {
                "photos": []
            }
        }

    @staticmethod
    def invalid_structure_response() -> Dict[str, Any]:
        """Mock response with invalid structure (missing keys)."""
        return {
            "email": "test.user@gmail.com",
            "username": "Test User"
            # Missing 'media' key
        }


class GoogleAPIErrorMocks:
    """Mock error responses from Google API."""

    @staticmethod
    def rate_limit_error() -> Dict[str, Any]:
        """Mock rate limit exceeded error."""
        return {
            "error": {
                "code": 429,
                "message": "Rate limit exceeded",
                "status": "RESOURCE_EXHAUSTED"
            }
        }

    @staticmethod
    def server_error() -> Dict[str, Any]:
        """Mock internal server error."""
        return {
            "error": {
                "code": 500,
                "message": "Internal server error",
                "status": "INTERNAL"
            }
        }

    @staticmethod
    def unauthorized_error() -> Dict[str, Any]:
        """Mock unauthorized access error."""
        return {
            "error": {
                "code": 401,
                "message": "Invalid or expired token",
                "status": "UNAUTHENTICATED"
            }
        }

    @staticmethod
    def not_found_error() -> Dict[str, Any]:
        """Mock resource not found error."""
        return {
            "error": {
                "code": 404,
                "message": "Resource not found",
                "status": "NOT_FOUND"
            }
        }


class MockResponseBuilder:
    """Builder for creating mock HTTP responses."""

    @staticmethod
    def build_success_response(data: Dict[str, Any], status_code: int = 200) -> Dict[str, Any]:
        """Build successful response structure."""
        return {
            "json": data,
            "status": status_code,
            "headers": {
                "Content-Type": "application/json",
                "X-Request-Id": "mock-request-123"
            }
        }

    @staticmethod
    def build_error_response(error_data: Dict[str, Any], status_code: int) -> Dict[str, Any]:
        """Build error response structure."""
        return {
            "json": error_data,
            "status": status_code,
            "headers": {
                "Content-Type": "application/json"
            }
        }

