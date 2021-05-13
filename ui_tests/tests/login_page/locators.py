from selenium.webdriver.common.by import By


class LoginPageLocators(object):
     USERNAME_FIELD = (By.ID, "user-name")
     PASSWORD_FIELD = (By.ID, "password")
     LOGIN_BUTTON = (By.XPATH, "//input[@id='login-button']")
     LOGIN_ERR_MSG = (By.XPATH, "//h3[@data-test='error']")