from gui_tests.utilities.locator_helper import LocatorHelper


class SidebarMenuLocators:
    """Locators for sidebar navigation menu."""
    ALL_ITEMS_LINK = LocatorHelper.by_id("inventory_sidebar_link")
    ABOUT_LINK = LocatorHelper.by_id("about_sidebar_link")
    LOGOUT_LINK = LocatorHelper.by_id("logout_sidebar_link")
    RESET_APP_LINK = LocatorHelper.by_id("reset_sidebar_link")
    CLOSE_MENU_BUTTON = LocatorHelper.by_id("react-burger-cross-btn")