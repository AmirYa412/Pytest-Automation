import time
from datetime import datetime, timedelta
from selenium.webdriver.remote.webdriver import WebDriver
from gui_tests.support.environment import Environment


class AuthHelper:
    """Helper for managing authentication state via cookies."""

    @staticmethod
    def auth_with_cookie(driver: WebDriver, env: Environment, user_key: str, cookies_cache: dict):
        """
        Inject authentication cookie for specified user to bypasses UI login for faster test setup.

        Args:
            driver : WebDriver instance
            env : Environment instance
            user_key: User key from environment.users (e.g., "standard_user")
            cookies_cache : cached cookies for re-use
        """
        try:
            user_data = env.users[user_key]
        except KeyError:
            raise KeyError(f"User '{user_key}' not found. Available users: {list(env.users.keys())}")

        driver.get(env.base_url) # Navigate to domain required to set cookies
        if user_key in cookies_cache: # Reuse cached authentication cookie if available
            for cookie in cookies_cache[user_key]:
                driver.add_cookie(cookie)
        else: # Inject new authentication cookie and cache it
            cookie = {
                'name': 'session-username',
                'value': user_data['username'],
                'path': '/',
                'domain': f".{env.domain.replace('www.', '')}",
                'secure': False,
                'httpOnly': False,
                'expiry': int((datetime.now() + timedelta(days=1)).timestamp()) # 1 day from now
            }
            driver.add_cookie(cookie)
            cookies_cache[user_key] = [cookie]

    @staticmethod
    def is_authenticated(driver: WebDriver) -> bool:
        """
        Check if driver has valid authentication cookie.

        Returns:
            True if authenticated, False otherwise
        """
        cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
        return 'session-username' in cookies

    @staticmethod
    def get_current_user(driver: WebDriver) -> str | None:
        """
        Get currently authenticated username.

        Returns:
            Username string if authenticated, None otherwise
        """
        cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
        return cookies.get('session-username')

    @staticmethod
    def logout(driver : WebDriver):
        """Clear authentication cookies."""
        driver.delete_cookie('session-username')
        driver.refresh()