from pytest import mark

pytestmark = [mark.gui, mark.inventory]


@mark.usefixtures("gui_test_class_setup")
class TestInventoryPage:
    def test_inventory_page_navigate_for_logged_in_user(self, pages):
        pages.authenticate(user="standard_user")
        pages.inventory.navigate()
        pages.inventory.header.is_logo_displayed()
        assert pages.inventory.are_items_titles_displayed()

    def test_sort_inventory_items_by_highest_price(self, pages):
        pages.authenticate(user="standard_user")
        pages.inventory.navigate()
        pages.inventory.click_sort_button()
        pages.inventory.choose_option(sort_by="hilo")
        assert pages.inventory.are_items_sorted_as_expected(sort_by="hilo")