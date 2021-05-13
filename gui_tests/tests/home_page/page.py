from gui_tests.utils.base_page import BasePage
from gui_tests.tests.home_page.locators import HomePageLocators


class HomePage(BasePage):

    def are_homepage_items_titles_displayed(self):
        try:
            return self.are_all_elments_displayed(HomePageLocators.HOMEPAGE_ITEM_TITLE)
        except Exception as e:
            raise Exception(e)

    def click_sort_button(self):
        try:
            return self.click_element(HomePageLocators.SORT_BUTTON)
        except Exception as e:
            raise Exception(e)

    def choose_option(self, sort_by):
        try:
            self.choose_option_from_dropdown_by_value(HomePageLocators.SORT_DROPDOWN_OPTIONS, sort_by)
        except Exception as e:
            raise Exception(e)

    def are_items_sorted_as_expected(self, sort_by):
        try:
            elements = self.driver.find_elements(*HomePageLocators.HOMEPAGE_ITEM_PRICE)
            for i in range(len(elements)-1):
                element1_price = float(elements[i].text.split("$")[1])
                element2_price = float(elements[i+1].text.split("$")[1])
                if sort_by == "hilo" and element1_price < element2_price:
                    return False
                elif sort_by == "lohi" and element1_price > element2_price:
                    return False
            return True

        except Exception as e:
            raise Exception(e)
