from selenium.webdriver.ie.webdriver import WebDriver
from gui_tests.pages.login.login_page import LoginPage
from gui_tests.pages.inventory.inventory_page import InventoryPage
from gui_tests.pages.shopping_cart.shopping_cart_page import ShoppingCartPage
from gui_tests.support.environment import Environment
from gui_tests.utilities.auth_helper import AuthHelper


class PageFactory:
    """Factory for lazy-loading page objects"""

    def __init__(self, driver: WebDriver, env: Environment ,auth_cookies_cache: dict):
        self._driver = driver
        self._env = env
        self._pages_cache = {}
        self._auth_cookies_cache = auth_cookies_cache
        self.auth_helper = AuthHelper

    def authenticate(self, user: str):
        """Authenticate user using LoginPage"""
        self.auth_helper.auth_with_cookie(self._driver, self._env ,user, self._auth_cookies_cache)

    @property
    def login(self) -> LoginPage:
        """Get or create LoginPage instance"""
        if 'login' not in self._pages_cache:
            self._pages_cache['login'] = LoginPage(self._driver, self._env)
        return self._pages_cache['login']

    @property
    def inventory(self) -> InventoryPage:
        """Get or create InventoryPage instance"""
        if 'inventory' not in self._pages_cache:
            self._pages_cache['inventory'] = InventoryPage(self._driver, self._env)
        return self._pages_cache['inventory']

    @property
    def shopping_cart(self) -> ShoppingCartPage:
        """Get or create ShoppingCartPage instance"""
        if 'shopping_cart' not in self._pages_cache:
            self._pages_cache['shopping_cart'] = ShoppingCartPage(self._driver, self._env)
        return self._pages_cache['shopping_cart']

