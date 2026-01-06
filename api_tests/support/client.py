from api_tests.support.environment import Environment
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import logging


TIMEOUT = 30
FORCE_RETRY_LIST = [502, 503, 504, 520, 524]


class Client:
    """HTTP client for API testing with automatic retry and session management.

    Provides methods for GET, POST, PUT, DELETE requests with built-in
    retry logic for transient failures and consistent session handling.
    """

    def __init__(self, env: Environment):
        self.env = env
        self.base_url = f"{self.env.protocol}{self.env.host}"
        self.api_ver = self.env.api_ver
        self.users = env.users
        self.session = requests.Session()
        self._default_headers = self.session.headers.copy()
        self.session.headers.update(self.env.headers)
        self.session.verify = False
        self._set_session_retries()
        self._set_requests_logging()

    def _set_session_retries(self):
        """Configure automatic retry strategy for transient failures."""
        retry_strategy = Retry(
            total=3,           # Total number of retries, for all response errors
            backoff_factor=1,  # Wait time between retries (1, 2, 4, 8 seconds...)
            status_forcelist=FORCE_RETRY_LIST,  # HTTP status codes to retry
            allowed_methods=["HEAD", "GET", "POST", "PUT", "DELETE", "OPTIONS", "TRACE"]
        )

        standard_adapter = HTTPAdapter(max_retries=retry_strategy, pool_connections=10, pool_maxsize=5)
        self.session.mount("https://", standard_adapter)

    @staticmethod
    def _set_requests_logging(level: int = logging.DEBUG):
        """
        Configure logging for requests and urllib3 libraries.
        Default to DEBUG for detailed requests timeline.
        """
        logging.getLogger("urllib3").setLevel(level)

    def post_request(self, path: str, data=None, params=None, files=None, json=None) -> requests.Response:
        try:
            response = self.session.post(f"{self.base_url}{self.api_ver}{path}",
                                         data=data,
                                         params=params,
                                         files=files,
                                         json=json,
                                         timeout=TIMEOUT)
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed POST request to {self.base_url}{self.api_ver}{path}, error: {e}")

    def get_request(self, path: str, params=None) -> requests.Response:
        try:
            response = self.session.get(f"{self.base_url}{self.api_ver}{path}",
                                        params=params,
                                        timeout=TIMEOUT)
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed GET request to {self.base_url}{self.api_ver}{path}, error: {e}")

    def put_request(self, path: str, data=None, json=None) -> requests.Response:
        try:
            response = self.session.put(f"{self.base_url}{self.api_ver}{path}",
                                        data=data, json=json, timeout=TIMEOUT)
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed PUT request, error: {e}")

    def delete_request(self, path: str) -> requests.Response:
        try:
            response = self.session.delete(f"{self.base_url}{self.api_ver}{path}",
                                           timeout=TIMEOUT)
            return response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed DELETE request, error: {e}")


    def reset_session(self):
        """Reset session headers and cookies to default state."""
        self.session.headers = self._default_headers.copy()
        self.session.headers.update(self.env.headers)
        self.session.cookies.clear()
