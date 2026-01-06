import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
from gui_tests.support.environment import Environment


class BasePage:
    PATH = "/"    # Default path, override by subclass
    TITLE = None  # Default title, override by subclass

    def __init__(self, driver: WebDriver, env: Environment):
        self.driver = driver
        self.env = env
        self.timeout = self.env.timeout
        self.logger = logging.getLogger(f"gui.{self.__class__.__name__}")

    def navigate(self, path: str=None, verify_on_page=True):
        """Navigate to page with optional validation."""
        target = path if path is not None else self.PATH
        self.logger.info(f"navigating to {target}")
        self.driver.get(f"{self.env.base_url}{target}")
        if verify_on_page:
            self.verify_on_page()
            self.verify_page_title()

    def verify_on_page(self):
        """Verify URL contains expected substring."""
        self.logger.info(f"verifying on correct path={self.PATH} by URL")
        current_url = self.driver.current_url
        assert self.PATH in current_url, f"Expected url {self.PATH}, but got {current_url}"

    def verify_page_title(self):
        """Verify page title matches TITLE attribute (if set)."""
        if self.TITLE and hasattr(self, 'header'):
            self.logger.info(f"verifying subtitle: {self.TITLE} on header")
            actual_title = self.header.get_page_title()
            assert actual_title == self.TITLE, f"Expected page title '{self.TITLE}', but got '{actual_title}'"

    def get_current_page_title(self) -> str:
        return self.driver.title

    def refresh_page(self):
        self.driver.refresh()

    # ========== WAIT METHODS (Return Elements) ==========

    def explicit_wait_element_visibility(self, locator, timeout: int = None) -> WebElement:
        """Wait for an element to be visible on the page.
        Returns the WebElement if found within the timeout period."""
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            error_msg = f"Element not visible after {timeout}s | Locator: {locator}\n URL: {self.driver.current_url}"
            raise TimeoutException(error_msg) from e

    def explicit_wait_element_clickable(self, locator, timeout: int = None) -> WebElement:
        """Wait for an element to be clickable on the page.
        Returns the WebElement if found within the timeout period."""
        timeout = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException as e:
            error_msg = f"Element not clickable after {timeout}s | Locator: {locator}\n URL: {self.driver.current_url}"
            raise TimeoutException(error_msg) from e

    # ========== ELEMENT INTERACTIONS ==========

    def is_element_displayed(self, locator) -> bool:
        element = self.explicit_wait_element_visibility(locator)
        return element.is_displayed()

    def get_element_text(self, locator) -> str:
        element = self.explicit_wait_element_visibility(locator)
        return element.text

    def send_text_to_element(self, locator, text : str):
        element = self.explicit_wait_element_visibility(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        element = self.explicit_wait_element_clickable(locator)
        element.click()

    def choose_option_from_dropdown_by_value(self, locator, value : str):
        element = self.explicit_wait_element_visibility(locator)
        dropdown = Select(element)
        dropdown.select_by_value(value)

    def hover_click_element(self, locator):
        element = self.explicit_wait_element_visibility(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()

    def hover_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click_element(self, element):
        ActionChains(self.driver).double_click(element).perform()

    def get_page_source_code(self) -> str:
        return self.driver.page_source