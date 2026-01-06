from pytest import mark

pytestmark = [mark.gui, mark.login]


@mark.usefixtures("gui_test_class_setup")
class TestLoginPage:

    def test_login_redirect_to_inventory_page(self, pages):
        pages.login.navigate()
        pages.login.perform_login(user="standard_user")
        pages.inventory.verify_on_page()
        assert pages.inventory.header.is_logo_displayed()

    def test_login_and_logout(self, pages):
        pages.login.navigate()
        pages.login.perform_login(user="standard_user")
        pages.inventory.verify_on_page()
        pages.inventory.header.click_sidebar_menu()
        pages.inventory.sidebar.click_logout()
        pages.login.verify_on_page()

    def test_red_err_msg_with_invalid_login_credentials(self, pages):
        pages.login.navigate()
        pages.login.perform_login(user="invalid_user")
        assert pages.login.is_err_msg_displayed()
