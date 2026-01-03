from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions



class BrowserFactory:
    """
    Modern Selenium 4 driver manager using built-in Selenium Manager.

    Args:
        browser: Browser name ('chrome', 'firefox', 'edge', 'safari')
        headless: Boolean, True by default
        maximize_window: Boolean, True by default
    """

    def __init__(self, browser, headless, maximize_window):
        self.browser = browser.lower()
        self.headless = headless
        self.maximize_window = maximize_window
        self._supported_browsers = {
            "chrome": self._chrome,
            "edge": self._edge,
            "firefox": self._firefox,
            "safari": self._safari
        }

    def create(self):
        """Get driver instance for specified browser."""
        if self.browser not in self._supported_browsers:
            raise ValueError(f"Unsupported browser: {self.browser}. Supported: {list(self._supported_browsers.keys())}")
        driver = self._supported_browsers[self.browser]()
        self._log_browser_info(driver)
        return driver

    def _chrome(self):
        """Create Chrome driver with current configuration."""
        options = ChromeOptions()
        self._configure_chromium_based_browser(options)
        return webdriver.Chrome(options=options)

    def _edge(self):
        """Create Edge driver with current configuration."""
        options = EdgeOptions()
        self._configure_chromium_based_browser(options)
        return webdriver.Edge(options=options)

    def _firefox(self):
        """Create Firefox driver with current configuration."""
        options = FirefoxOptions()
        if self.headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        if self.maximize_window:
            driver.maximize_window()
        return driver

    def _safari(self):
        """Create Safari driver (macOS only)."""
        driver = webdriver.Safari()
        if self.maximize_window:
            driver.maximize_window()
        return driver

    def _configure_chromium_based_browser(self, options):
        """Apply common configurations to Chromium-based drivers."""
        if self.headless:
            options.add_argument("--headless=new")

        # Window management
        if self.maximize_window:
            options.add_argument("--start-maximized")

        # UI improvements
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")

        # Anti-detection
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # Disable password manager
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile": {"password_manager_enabled": False}
        })

        # Docker/CI compatibility
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    def _log_browser_info(self, driver):
        """
        Log browser version and configuration details.
        TODO: Replace print with proper logger when logging is implemented.
        """
        try:
            caps = driver.capabilities
            browser_name = caps.get('browserName', 'Unknown')
            browser_version = caps.get('browserVersion') or caps.get('version', 'Unknown')
            platform_name = caps.get('platformName', 'Unknown')
            print(f"{'=' * 60}\nBROWSER SESSION INFO\n{'=' * 60}")
            print(f"Browser:      {browser_name.title()} {browser_version}")
            print(f"Platform:     {platform_name}")
            print(f"Headless:     {self.headless}")
            print(f"Maximized:    {self.maximize_window}")
        except Exception as e:
            print(f"Warning: Could not log browser info: {e}")
