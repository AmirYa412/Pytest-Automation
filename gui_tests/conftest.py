from pytest import fixture
from gui_tests.factories.pages import PageFactory
from gui_tests.factories.browser import BrowserFactory
from gui_tests.support.environment import Environment


def pytest_addoption(parser):
    parser.addoption("--gui_env", action="store", default=None, help="Invalid ENV")
    parser.addoption("--browser", action="store", default=None, help="Invalid browser")
    parser.addoption("--headless", action="store_true", help="run in headless")
    parser.addoption("--maximize", action="store_true", help="maximize window")


@fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    if not browser:
        browser = "chrome" # Default to Chrome if --browser not provided
        # browser = "firefox"
        # browser = "edge"
        # browser = "safari"
    return browser


@fixture(scope="session")
def env(request):
    """Determine which environment will be tested by domain prefix"""
    env_prefix = request.config.getoption("--gui_env")   # Terminal Option
    if not env_prefix:
        env_prefix = "www"
        # env_prefix = "qa" # Override to qa env
        # env_prefix = "dev"
    return Environment(env_prefix)


@fixture(scope="function")
def driver(browser, env, request):
    headless = request.config.getoption("--headless")
    maximize_window = request.config.getoption("--maximize")
    driver_manager = BrowserFactory(browser=browser, headless=headless, maximize_window=maximize_window)
    driver = driver_manager.create()
    driver.env = env
    yield driver
    driver.quit()


@fixture(scope="session")
def log():
    return None     # TODO Add logger


@fixture(scope="session")
def data():
    return None     # TODO Add data file per env


@fixture
def pages(driver, auth_cookies_cache) -> PageFactory:
    """Create page object factory"""
    return PageFactory(driver, auth_cookies_cache)


@fixture(scope="session")
def auth_cookies_cache():
    """
    Session-scoped cache for authentication cookies.
    Stores cookies per user to avoid repeated authentication.
    """
    return {}


@fixture(scope="class")
def gui_test_class_setup(request, data, log):
    request.cls.data = data
    request.cls.log = log
