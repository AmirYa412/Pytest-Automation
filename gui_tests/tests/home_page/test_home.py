import pytest
from gui_tests.pages.home.home_page import HomePage

pytestmark = pytest.mark.gui


@pytest.mark.usefixtures("gui_test_class_setup")
class TestHomePage:
    def test_items_titles_displayed(self, driver):
        client = HomePage(driver, self.env)
        client.perform_login(user="standard_user")
        assert client.are_homepage_items_titles_displayed()

    def test_order_homepage_items_by_highest_price(self, driver):
        client = HomePage(driver, self.env)
        client.perform_login(user="standard_user")
        client.click_sort_button()
        client.choose_option(sort_by="hilo")
        assert client.are_items_sorted_as_expected(sort_by="hilo")