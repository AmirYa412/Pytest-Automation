from gui_tests.utilities.locator_helper import LocatorHelper
from gui_tests.pages.base_page import BasePage
from gui_tests.pages.inventory.locators import InventoryPageLocators
from gui_tests.components.header.header import Header
from gui_tests.components.sidebar_menu.sidebar_menu import SidebarMenu

class InventoryPage(BasePage):
    PATH = "/inventory.html"
    TITLE = "Products"

    def __init__(self, driver, env):
        super().__init__(driver, env)
        self.header = Header(self)
        self.sidebar = SidebarMenu(self)

    def are_items_titles_displayed(self):
        return self.is_element_displayed(InventoryPageLocators.INVENTORY_ITEM_TITLE)

    def add_item_to_cart(self, item_name: str):
        """Add an item to cart by its name."""
        normalized_name = item_name.lower().replace(' ', '-')
        data_test_value = f"add-to-cart-{normalized_name}"
        add_button_locator = LocatorHelper.by_data_test(data_test_value)
        self.click_element(add_button_locator)

    def click_sort_button(self):
        return self.click_element(InventoryPageLocators.SORT_DROPDOWN)

    def choose_option(self, sort_by):
        self.choose_option_from_dropdown_by_value(InventoryPageLocators.SORT_DROPDOWN, sort_by)

    def are_items_sorted_as_expected(self, sort_by):
        elements = self.driver.find_elements(*InventoryPageLocators.INVENTORY_ITEM_PRICE)
        for i in range(len(elements)-1):
            element1_price = float(elements[i].text.split("$")[1])
            element2_price = float(elements[i+1].text.split("$")[1])
            if sort_by == "hilo" and element1_price < element2_price:
                return False
            elif sort_by == "lohi" and element1_price > element2_price:
                return False
        return True

