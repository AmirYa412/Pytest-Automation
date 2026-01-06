from api_tests.support.users import PRODUCTION_USERS, CI_USERS

CI_ENVS_PREFIXES = ("qa", "dev")


class Environment:
    """Configuration for API test environment.

    Manages environment-specific settings including base URLs, headers,
    and user credentials for both CI and production environments.
    """


    def __init__(self, env_prefix: str):
        self.env_prefix = env_prefix
        self.protocol = "https://"
        self.host = f"{self.env_prefix}.swagger.io"
        self.api_ver = "/v2"
        self.is_ci_env = True if env_prefix in CI_ENVS_PREFIXES else False
        self.headers = self._set_env_headers()
        self.users = self.get_automation_users()

    def _set_env_headers(self):
        return {
            "Accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9,",
            "Connection": "keep-alive",
            "Host": f"{self.env_prefix}.swagger.io",
            "Origin": f"https://{self.env_prefix}.swagger.io",
            "Referer": f"https://{self.env_prefix}.swagger.io/",
            "Content-Type": "application/json; charset=utf-8",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Upgrade-Insecure-Requests": "1"
        }

    def get_automation_users(self):
        """Get automation user credentials for the current environment.

        Returns:
            Dictionary of user credentials

        Raises:
            EnvironmentError: If any user is missing a password
        """
        users = CI_USERS if self.is_ci_env else PRODUCTION_USERS
        if any(user.get("password") is None for user in users.values()):
            raise EnvironmentError(f"Test users are missing passwords. {self.env_prefix} | {users}")
        return users