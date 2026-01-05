from gui_tests.pages.base_page import BasePage
from gui_tests.pages.shopping_cart.locators import ShoppingCartPageLocators


class ShoppingCartPage(BasePage):
    PATH = "/cart.html"
    TITLE = "Your Cart"

    def is_item_in_cart(self, item_name: str) -> bool:
        """Check if a specific item is present in the cart."""
        cart_items = self.get_cart_item_names()
        return item_name in cart_items

    def get_cart_item_names(self) -> list[str]:
        """Get list of all item names currently in the cart."""
        elements = self.driver.find_elements(*ShoppingCartPageLocators.CART_ITEM_NAME)
        return [element.text for element in elements]

    def get_cart_item_count(self) -> int:
        """Get the number of items currently in the cart."""
        elements = self.driver.find_elements(*ShoppingCartPageLocators.CART_ITEMS)
        return len(elements)
