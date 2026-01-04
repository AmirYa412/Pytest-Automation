import pytest

pytestmark = pytest.mark.gui


@pytest.mark.usefixtures("gui_test_class_setup")
class TestLoginPage:

    def test_login_redirect_to_homepage(self, pages):
        pages.login.navigate()
        pages.login.perform_login(user="standard_user")
        assert "/inventory.html" in pages.login.driver.current_url
        assert pages.home.is_home_logo_displayed()

    def test_red_err_msg_with_invalid_login_credentials(self, pages):
        pages.login.navigate()
        pages.login.perform_login(user="invalid_user")
        assert pages.login.is_err_msg_displayed()
