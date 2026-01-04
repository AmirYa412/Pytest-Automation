import pytest

pytestmark = pytest.mark.gui


@pytest.mark.usefixtures("gui_test_class_setup")
class TestHomePage:
    def test_items_titles_displayed(self, pages):
        pages.authenticate(user="standard_user")
        pages.home.navigate()
        assert pages.home.are_homepage_items_titles_displayed()

    def test_order_homepage_items_by_highest_price(self, pages):
        pages.authenticate(user="standard_user")
        pages.home.navigate()
        pages.home.click_sort_button()
        pages.home.choose_option(sort_by="hilo")
        assert pages.home.are_items_sorted_as_expected(sort_by="hilo")