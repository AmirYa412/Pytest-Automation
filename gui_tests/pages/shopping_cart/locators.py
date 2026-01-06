from gui_tests.utilities.locator_helper import LocatorHelper


class ShoppingCartPageLocators:
    CART_ITEMS = LocatorHelper.by_class("cart_item")
    CART_ITEM_NAME = LocatorHelper.by_class("inventory_item_name")
    CART_ITEM_PRICE = LocatorHelper.by_class("inventory_item_price")
    CART_ITEM_QUANTITY = LocatorHelper.by_class("cart_quantity")