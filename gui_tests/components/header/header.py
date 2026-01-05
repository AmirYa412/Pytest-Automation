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
        self.page.click_element(HeaderLocators.SHOPPING_CART_BUTTON)

    def click_sidebar_menu(self):
        """Open burger menu (sidebar)."""
        self.page.click_element(HeaderLocators.SIDEBAR_MENU_BUTTON)

    def get_page_title(self) -> str:
        """Get the title text from the header."""
        return self.page.get_element_text(HeaderLocators.PAGE_TITLE)

    def get_cart_item_count(self) -> int:
        """Get the number of items in the shopping cart badge."""
        badge_text = self.page.get_element_text(HeaderLocators.SHOPPING_CART_BADGE)
        return int(badge_text)
