from gui_tests.utils.base_page import BasePage
from gui_tests.pages.locators.login_page_locators import LoginPageLocators
from gui_tests.pages.locators.home_page_locators import HomePageLocators


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

