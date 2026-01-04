from gui_tests.pages.login.login_page import LoginPage
from gui_tests.pages.home.home_page import HomePage
from gui_tests.utilities.auth_helper import AuthHelper


class PageFactory:
    """Factory for lazy-loading page objects"""

    def __init__(self, driver, auth_cookies_cache: dict):
        self._driver = driver
        self._pages_cache = {}
        self._auth_cookies_cache = auth_cookies_cache
        self.auth_helper = AuthHelper

    def authenticate(self, user: str):
        """Authenticate user using LoginPage"""
        self.auth_helper.auth_with_cookie(self._driver, user, self._auth_cookies_cache)

    @property
    def login(self) -> LoginPage:
        """Get or create LoginPage instance"""
        if 'login' not in self._pages_cache:
            self._pages_cache['login'] = LoginPage(self._driver)
        return self._pages_cache['login']

    @property
    def home(self) -> HomePage:
        """Get or create HomePage instance"""
        if 'home' not in self._pages_cache:
            self._pages_cache['home'] = HomePage(self._driver,)
        return self._pages_cache['home']

