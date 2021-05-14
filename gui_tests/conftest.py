import pytest
from gui_tests.drivers.get_driver import DriverManager
from gui_tests.core.set_environment import TestedEnvironment


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=None, help="Invalid ENV")
    parser.addoption("--browser", action="store", default=None, help="Invalid browser")


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    if not browser:
        browser = "chrome"
        # browser = "firefox"
        # browser = "edge"
    return browser


@pytest.fixture(scope="session")
def env(request):
    """Determine which environment driver send requests to """
    env_prefix = request.config.getoption("--env")   # Terminal Option
    if not env_prefix:
        env_prefix = "www"  # Overide to production env
        # env_prefix = "qa"
        # env_prefix = "dev"  # Overide to dev env
    return TestedEnvironment(env_prefix)


@pytest.fixture(scope="function")
def driver(browser):
    driver_manager = DriverManager(browser)
    driver = driver_manager.get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def log():
    return None     # TODO Add logger


@pytest.fixture(scope="session")
def data():
    return None     # TODO Add data file per env


@pytest.fixture(scope="class")
def gui_test_class_setup(request, env, data, log):
    request.cls.env = env
    request.cls.data = data
    request.cls.log = log

