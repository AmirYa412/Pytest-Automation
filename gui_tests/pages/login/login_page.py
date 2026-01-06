from gui_tests.pages.base_page import BasePage
from gui_tests.pages.login.locators import LoginPageLocators


class LoginPage(BasePage):
    """Page object for the Login Page."""
    PATH = "/"
    TITLE = None

    def __init__(self, driver, env):
        super().__init__(driver, env)

    def perform_login(self, user: str):
        try:
            user_credentials = self.env.users[user]
        except KeyError:
            raise KeyError(f"Wrong user key provided. Environment: {self.env} Available users: {self.env.users.keys()}")
        self.send_text_to_element(locator=LoginPageLocators.USERNAME_FIELD, text=user_credentials["username"])
        self.send_text_to_element(locator=LoginPageLocators.PASSWORD_FIELD, text=user_credentials["password"])
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def is_err_msg_displayed(self) -> bool:
        return self.is_element_displayed(LoginPageLocators.LOGIN_ERR_MSG)

