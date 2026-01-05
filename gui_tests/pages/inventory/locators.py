from gui_tests.utilities.locator_helper import LocatorHelper


class InventoryPageLocators(object):
    INVENTORY_ITEM_TITLE = LocatorHelper.by_class("inventory_item_name")
    INVENTORY_ITEM_PRICE = LocatorHelper.by_class("inventory_item_price")
    SORT_DROPDOWN = LocatorHelper.by_data_test("product-sort-container")
