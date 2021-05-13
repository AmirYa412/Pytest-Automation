from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

_HOME_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DriverManager:
    def __init__(self, browser):
        self.browser = browser
        self.supported_browsers = {
            "chrome": self.get_local_chromedriver,
            "firefox": self.get_local_firefox,
            "explorer": self.get_local_internet_explorer
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
            driver = webdriver.Chrome(executable_path=os.path.join(_HOME_PATH, "Drivers", "chromedriver.exe"), options=options)
        return driver

    @staticmethod
    def get_local_firefox():
        try:
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        except BaseException:
            driver = webdriver.Firefox(executable_path=os.path.join(_HOME_PATH, "Drivers", "geckodriver.exe"))
        return driver

    @staticmethod
    def get_local_internet_explorer():
        try:
            driver = webdriver.Ie(IEDriverManager().install())
        except BaseException:
            driver = webdriver.Ie(os.path.join(_HOME_PATH, "Drivers", "IEDriverServer.exe"))
        return driver