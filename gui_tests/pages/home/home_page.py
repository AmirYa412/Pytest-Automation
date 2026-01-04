from gui_tests.pages.base_page import BasePage
from gui_tests.pages.home.locators import HomePageLocators


class HomePage(BasePage):
    PATH = "/inventory.html"

    def navigate_home(self):
        self.navigate(self.PATH)

    def are_homepage_items_titles_displayed(self):
        return self.is_element_displayed(HomePageLocators.HOMEPAGE_ITEM_TITLE)

    def is_home_logo_displayed(self):
        return self.is_element_displayed(HomePageLocators.HOMEPAGE_MAIN_LOGO)


    def click_sort_button(self):
        return self.click_element(HomePageLocators.SORT_DROPDOWN)

    def choose_option(self, sort_by):
        self.choose_option_from_dropdown_by_value(HomePageLocators.SORT_DROPDOWN, sort_by)

    def are_items_sorted_as_expected(self, sort_by):
        elements = self.driver.find_elements(*HomePageLocators.HOMEPAGE_ITEM_PRICE)
        for i in range(len(elements)-1):
            element1_price = float(elements[i].text.split("$")[1])
            element2_price = float(elements[i+1].text.split("$")[1])
            if sort_by == "hilo" and element1_price < element2_price:
                return False
            elif sort_by == "lohi" and element1_price > element2_price:
                return False
        return True

