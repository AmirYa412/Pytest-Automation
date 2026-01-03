import pytest
from gui_tests.drivers.browser_factory import BrowserFactory
from gui_tests.core.set_environment import TestedEnvironment


def pytest_addoption(parser):
    parser.addoption("--gui_env", action="store", default=None, help="Invalid ENV")
    parser.addoption("--browser", action="store", default=None, help="Invalid browser")
    parser.addoption("--headless", action="store_true", help="run in headless")
    parser.addoption("--maximize", action="store_true", help="maximize window")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    if not browser:
        browser = "chrome" # Default to Chrome if not arg provided
        # browser = "firefox"
        # browser = "edge"
        # browser = "safari"
    return browser


@pytest.fixture(scope="session")
def env(request):
    """Determine which environment driver send requests to """
    env_prefix = request.config.getoption("--gui_env")   # Terminal Option
    if not env_prefix:
        env_prefix = "www"
        # env_prefix = "qa" # Override to qa env
        # env_prefix = "dev"
    return TestedEnvironment(env_prefix)


@pytest.fixture(scope="function")
def driver(browser, env, request):
    headless = request.config.getoption("--headless")
    maximize_window = request.config.getoption("--maximize")
    driver_manager = BrowserFactory(browser=browser, headless=headless, maximize_window=maximize_window)
    driver = driver_manager.create()
    driver.env = env
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def log():
    return None     # TODO Add logger


@pytest.fixture(scope="session")
def data():
    return None     # TODO Add data file per env


@pytest.fixture(scope="class")
def gui_test_class_setup(request, data, log):
    request.cls.data = data
    request.cls.log = log

