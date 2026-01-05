from pytest import mark


@mark.usefixtures("gui_test_class_setup")
class TestShoppingCartPage:
    def test_add_2_items_to_shopping_cart(self, pages ,data):
        pages.authenticate(user="standard_user")
        pages.inventory.navigate()
        assert pages.inventory.are_items_titles_displayed()
        pages.inventory.add_item_to_cart(data["inventory"]["item_1"])
        pages.inventory.add_item_to_cart(data["inventory"]["item_2"])
        assert pages.inventory.header.get_cart_item_count() == 2

        pages.inventory.header.click_shopping_cart()
        pages.shopping_cart.verify_on_page()
        assert pages.shopping_cart.is_item_in_cart(data["inventory"]["item_1"])
        assert pages.shopping_cart.is_item_in_cart(data["inventory"]["item_2"])
        assert pages.shopping_cart.get_cart_item_count() == 2

