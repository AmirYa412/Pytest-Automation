# gui_tests/components/header.py
from gui_tests.pages.base_page import BasePage
from gui_tests.components.header.locators import HeaderLocators


class Header:
    """Header component - appears on all authenticated pages."""

    def __init__(self, base_page: BasePage):
        """
        Initialize header component.

        Args:
            base_page: BasePage instance to access driver and common methods
        """
        self.page = base_page

    def is_logo_displayed(self):
        """Check if app logo is visible."""
        return self.page.is_element_displayed(HeaderLocators.APP_LOGO)

    def click_shopping_cart(self):
        """Click shopping cart icon."""
        self.page.click_element(HeaderLocators.SHOPPING_CART_LINK)

    def get_cart_item_count(self):
        """Get number of items in cart from badge."""
        return self.page.get_element_text(HeaderLocators.SHOPPING_CART_BADGE)

    def open_menu(self):
        """Open burger menu (sidebar)."""
        self.page.click_element(HeaderLocators.BURGER_MENU_BUTTON)