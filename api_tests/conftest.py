import pytest
from api_tests.support.environment import TestedEnvironment


def pytest_addoption(parser):
    parser.addoption("--api_env", action="store", default=None, help="Invalid env prefix")


@pytest.fixture(scope="session")
def env(request):
    """Determine to which ClientSession will send requests to """
    env_prefix = request.config.getoption("--api_env")   # Terminal Option
    if not env_prefix:
        env_prefix = "petstore"                  # Override PROD  env
        # env_prefix = "qa-petstore"             # Override to dummy QA env
        # env_prefix = "dev-petstore"            # Override to dummy DEV env
    return TestedEnvironment(env_prefix)


@pytest.fixture(scope="class")
def api_test_class_setup(request, env):
    request.cls.env = env
