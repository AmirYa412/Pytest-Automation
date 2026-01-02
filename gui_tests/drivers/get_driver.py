from gui_tests.core.set_environment import _GUI_PROJECT_ROOT
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

_GUI_PROJECT_ROOT

class DriverManager:
    def __init__(self, browser):
        self.browser = browser
        self.supported_browsers = {
            "chrome": self.get_local_chromedriver,
            "firefox": self.get_local_firefox,
            "edge": self.get_local_edge
        }

    def get_driver(self):
        return self.supported_browsers[self.browser]()

    @staticmethod
    def get_local_chromedriver():
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["disable-logging"])     # Disable Bluetooth error
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('prefs', {      # Disable Save password window
            'credentials_enable_service': False,
            'profile': {'password_manager_enabled': False}})
        try:
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        except BaseException:
            # If failed to install, will try using local file
            driver = webdriver.Chrome(executable_path=os.path.join(_GUI_PROJECT_ROOT, "drivers", "chrome","chromedriver.exe"), options=options)
        return driver

    @staticmethod
    def get_local_firefox():
        try:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        except BaseException:
            driver = webdriver.Firefox(executable_path=os.path.join(_GUI_PROJECT_ROOT, "drivers", "firefox", "geckodriver.exe"))
        driver.maximize_window()
        return driver

    @staticmethod
    def get_local_edge():
        try:
            driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        except BaseException:
            driver = webdriver.Edge(os.path.join(_GUI_PROJECT_ROOT, "drivers", "edge", "msedgedriver.exe"))
        return driver