from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from gui_tests.tests.login_page.locators import LoginPageLocators
import time
from random import randint
import string


class BasePage:
    def __init__(self, driver: WebDriver, env=None, ):
        self.driver = driver
        self.env = env
        self.navigate()

    def navigate(self, path="/"):
        self.driver.get(self.env.host + path)

    def perform_login(self, user):
        try:
            user_credentials = self.env.users[user]
            self.send_text_to_element(locator=LoginPageLocators.USERNAME_FIELD, text=user_credentials["username"])
            self.send_text_to_element(locator=LoginPageLocators.PASSWORD_FIELD, text=user_credentials["password"])
            self.click_element(LoginPageLocators.LOGIN_BUTTON)
        except Exception as e:
            raise Exception(e)

    def get_current_page_title(self):
        try:
            return self.driver.title
        except BaseException as e:
            raise BaseException(e)

    def refresh_page(self):
        try:
            self.driver.refresh()
        except BaseException as e:
            raise BaseException(e, 'Couldnt refresh page')

    def explicit_wait_element_visibilty(self, sec, locator):
        try:
            WebDriverWait(self.driver, sec).until(EC.visibility_of_element_located(locator))
        except BaseException as e:
            raise NoSuchElementException(e)

    def is_element_displayed(self, locator):
        try:
            self.explicit_wait_element_visibilty(5, locator)
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except Exception as e:
            raise NoSuchElementException(e)

    def are_all_elments_displayed(self, locator):
        try:
            self.explicit_wait_element_visibilty(5, locator)
            elements = self.driver.find_elements(*locator)
            for ele in elements:
                if not ele.is_displayed():
                    return False
            return True
        except Exception as e:
            raise NoSuchElementException(e)

    def get_element_text(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.text
        except Exception as e:
            raise NoSuchElementException(e)

    def send_text_to_element(self, locator, text):
        try:
            self.explicit_wait_element_visibilty(5, locator)
            element = self.driver.find_element(*locator)
            element.send_keys(text)
            time.sleep(1)
        except Exception as e:
            raise NoSuchElementException(e)

    def click_element(self, locator):
        try:
            self.explicit_wait_element_visibilty(5, locator)
            element = self.driver.find_element(*locator)
            element.click()
        except Exception as e:
            raise NoSuchElementException(e)

    def choose_option_from_dropdown_by_value(self, locator, value):
        try:
            self.explicit_wait_element_visibilty(5, locator)
            dropdown = Select(self.driver.find_element(*locator))  # Handle dropdowns with SELECT html attribute
            dropdown.select_by_value(value)
        except Exception as e:
            raise NoSuchElementException(e)

    def hover_click_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
            ActionChains(self.driver).move_to_element(element).perform()
            element.click()
        except Exception as e:
            raise NoSuchElementException(e)

    def hover_element(self, element):
        try:
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            raise NoSuchElementException(e)

    def double_click_element(self, element):
        try:
            ActionChains(self.driver).double_click(element).perform()
        except Exception as e:
            raise NoSuchElementException(e)

    def scroll_to_given_offset(self, offest: int):
        try:
            self.driver.execute_script("window.scrollTo(0, %d)" % offest)
            time.sleep(1.5)
        except Exception as e:
            raise NoSuchElementException(e)

    def get_page_source_code(self):
        try:
            return self.driver.page_source
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def random_num(minimum, maximum):
        return randint(minimum, maximum)

    @staticmethod
    def get_random_str(length: int):
        characters = string.ascii_letters + string.digits
        return ''.join([characters[randint(0, len(characters)-1)] for i in range(length)])
