# gui_tests/components/sidebar_menu.py
from gui_tests.pages.base_page import BasePage
from gui_tests.components.sidebar_menu.locators import SidebarMenuLocators


class SidebarMenu:
    """Sidebar navigation menu component."""

    def __init__(self, base_page: BasePage):
        self.page = base_page

    def click_all_items(self):
        """Navigate to all items (inventory page)."""
        self.page.click_element(SidebarMenuLocators.ALL_ITEMS_LINK)

    def click_about(self):
        """Navigate to About page."""
        self.page.click_element(SidebarMenuLocators.ABOUT_LINK)

    def click_logout(self):
        """Logout from application."""
        self.page.click_element(SidebarMenuLocators.LOGOUT_LINK)

    def click_reset_app(self):
        """Reset application state."""
        self.page.click_element(SidebarMenuLocators.RESET_APP_LINK)

    def close_menu(self):
        """Close sidebar menu."""
        self.page.click_element(SidebarMenuLocators.CLOSE_MENU_BUTTON)