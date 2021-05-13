from gui_tests.utils.base_page import BasePage
from gui_tests.tests.login_page.locators import LoginPageLocators
from gui_tests.tests.home_page.locators import HomePageLocators


class LoginPage(BasePage):

    def is_home_logo_displayed(self):
        try:
            return self.is_element_displayed(HomePageLocators.HOMEPAGE_MAIN_LOGO)
        except Exception as e:
            raise Exception(e)

    def is_err_msg_displayed(self):
        try:
            return self.is_element_displayed(LoginPageLocators.LOGIN_ERR_MSG)
        except Exception as e:
            raise Exception(e)

