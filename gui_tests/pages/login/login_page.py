from gui_tests.pages.base_page import BasePage
from gui_tests.pages.login.locators import LoginPageLocators


class LoginPage(BasePage):
    PATH = "/"
    TITLE = None

    def perform_login(self, user):
        try:
            user_credentials = self.env.users[user]
        except KeyError:
            raise KeyError(f"Wrong user key provided. Environment: {self.env} Available users: {self.env.users.keys()}")
        self.send_text_to_element(locator=LoginPageLocators.USERNAME_FIELD, text=user_credentials["username"])
        self.send_text_to_element(locator=LoginPageLocators.PASSWORD_FIELD, text=user_credentials["password"])
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def is_err_msg_displayed(self):
        return self.is_element_displayed(LoginPageLocators.LOGIN_ERR_MSG)

