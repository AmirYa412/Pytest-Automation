from gui_tests.utilities.locator_helper import LocatorHelper


class LoginPageLocators:
     USERNAME_FIELD = LocatorHelper.by_id("user-name")
     PASSWORD_FIELD = LocatorHelper.by_id("password")
     LOGIN_BUTTON = LocatorHelper.by_id("login-button")
     LOGIN_ERR_MSG = LocatorHelper.by_data_test("error")
