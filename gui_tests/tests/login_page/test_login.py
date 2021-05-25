import pytest
from gui_tests.pages.login.login_page import LoginPage

pytestmark = pytest.mark.gui


@pytest.mark.usefixtures("gui_test_class_setup")
class TestLoginPage:
    def test_login_redirect_to_homepage(self, driver):
        client = LoginPage(driver, self.env)
        client.perform_login(user="standard_user")
        assert client.is_home_logo_displayed()
        assert "/inventory.html" in client.driver.current_url

    def test_red_err_msg_with_invalid_login_credentials(self, driver):
        client = LoginPage(driver, self.env)
        client.perform_login(user="invalid_user")
        assert client.is_err_msg_displayed()
