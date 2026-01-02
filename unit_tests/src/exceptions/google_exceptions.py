class GoogleAPIError(Exception):
    """Base exception for all Google API related errors."""
    pass


class GoogleAuthError(GoogleAPIError):
    """Raised when authentication fails."""
    pass


class TokenExpiredError(GoogleAuthError):
    """Raised when the authentication token has expired."""
    pass


class GooglePhotosFetchError(GoogleAPIError):
    """Raised when fetching photos fails."""
    pass


class RateLimitError(GoogleAPIError):
    """Raised when API rate limit is exceeded."""
    pass


class PaginationError(GoogleAPIError):
    """Raised when pagination logic fails."""
    pass


class InvalidResponseError(GoogleAPIError):
    """Raised when API response format is invalid."""
    pass