def pytest_addoption(parser):
    # gui_tests options
    parser.addoption("--gui_env", action="store", default=None, help="Invalid ENV")
    parser.addoption("--browser", action="store", default=None, help="Invalid browser")
    parser.addoption("--headless", action="store_true", help="run in headless")
    parser.addoption("--maximize", action="store_true", help="maximize window")

    # api_tests options
    parser.addoption("--api_env", action="store", default=None, help="API environment prefix")


