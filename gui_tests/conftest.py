from pathlib import Path
import json
from pytest import fixture
from pytest import mark
from gui_tests.factories.pages import PageFactory
from gui_tests.factories.browser import BrowserFactory
from gui_tests.support.environment import Environment
from gui_tests.logger import LoggerFactory

GUI_PROJECT_ROOT = Path(__file__).parent.resolve()


def pytest_addoption(parser):
    parser.addoption("--gui_env", action="store", default=None, help="Invalid ENV")
    parser.addoption("--browser", action="store", default=None, help="Invalid browser")
    parser.addoption("--headless", action="store_true", help="run in headless")
    parser.addoption("--maximize", action="store_true", help="maximize window")


@fixture(scope="session")
def env(request):
    """Determine which environment will be tested by domain prefix"""
    env_prefix = request.config.getoption("--gui_env")   # Terminal Option
    if not env_prefix:
        env_prefix = "www"
        # env_prefix = "qa" # Override to qa env
        # env_prefix = "dev"
    return Environment(env_prefix)


@fixture(scope="session")
def browser(request):
    """Get browser name from CLI option or use default."""
    browser = request.config.getoption("--browser")
    if not browser:
        browser = "chrome" # Default to Chrome if --browser not provided
        # browser = "firefox"
        # browser = "edge"
        # browser = "safari"
    return browser


@fixture(scope="function")
def driver(browser, request):
    """Create WebDriver instance for test."""
    headless = request.config.getoption("--headless")
    maximize_window = request.config.getoption("--maximize")
    driver_manager = BrowserFactory(browser=browser, headless=headless, maximize_window=maximize_window)
    driver = driver_manager.create()
    yield driver
    driver.quit()


@fixture(scope="session", autouse=True)
def logger():
    """Session-scoped logger."""
    return LoggerFactory(project="gui")

@fixture(scope="session")
def data(env):
    hardcoded_filename = "production.json"
    if env.is_ci:
        hardcoded_filename = "ci.json"
    file_path = Path(GUI_PROJECT_ROOT) / "hardcoded_data" / hardcoded_filename
    with open(file_path, 'r') as f:
        return json.load(f)


@fixture
def pages(driver, env, auth_cookies_cache) -> PageFactory:
    """Create page object factory"""
    return PageFactory(driver, env, auth_cookies_cache)


@fixture(scope="session")
def auth_cookies_cache():
    """
    Session-scoped cache for authentication cookies.
    Stores cookies per user to avoid repeated authentication.
    """
    return {}


@fixture(scope="class")
def gui_test_class_setup(request, data):
    request.cls.data = data


###############################################################
# REPORTING CONFIGURATIONS
###############################################################

@fixture(scope="session", autouse=True)
def update_metadata(metadata, browser):
    try:
        """Adds metadata to HTML report"""
        metadata['Browser'] = browser.capitalize()
    except Exception as e:
        print(f"Failed to add browser metadata to report {e}")


@fixture(scope="function", autouse=True)
def log_test_execution(request, logger):
    """Log test start and end automatically."""
    test_name = request.node.name
    logger.info(f"*** TEST {test_name} STARTING")
    yield  # Test runs here
    logger.info(f"*** TEST {test_name} ENDED")


@mark.hookwrapper
def pytest_runtest_makereport(item):
    """Hook to access test execution status. Used to attach screenshot on failure"""
    try:
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' and report.failed:
            if 'driver' in item.fixturenames:
                driver = item.funcargs['driver']
                screenshot_base64 = driver.get_screenshot_as_base64()
                extra.append(pytest_html.extras.image(screenshot_base64, mime_type='image/png'))
        report.extra = extra
    except Exception as e:
        print(f"Error in taking screenshot: {e}")
