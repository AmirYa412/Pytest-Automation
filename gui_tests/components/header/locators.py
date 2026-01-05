from gui_tests.utilities.locator_helper import LocatorHelper


class HeaderLocators(object):
    """Locators for header component."""
    APP_LOGO = LocatorHelper.by_class("app_logo")
    PAGE_TITLE = LocatorHelper.by_class("title")
    SHOPPING_CART_BUTTON = LocatorHelper.by_data_test("shopping-cart-link")
    SIDEBAR_MENU_BUTTON = LocatorHelper.by_id("react-burger-menu-btn")
