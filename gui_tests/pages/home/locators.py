from gui_tests.utilities.locator_helper import LocatorHelper


class HomePageLocators(object):
    HOMEPAGE_MAIN_LOGO = LocatorHelper.by_class("app_logo")
    HOMEPAGE_ITEM_TITLE = LocatorHelper.by_class("inventory_item_name")
    HOMEPAGE_ITEM_PRICE = LocatorHelper.by_class("inventory_item_price")
    SORT_DROPDOWN = LocatorHelper.by_data_test("product-sort-container")
