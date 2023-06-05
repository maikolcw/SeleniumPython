import pytest


# Defining fixtures in every test file can quickly get tedious and reduce code readability. An alternative is to put our
# fixtures in conftest.py where we can access the functions from every test file.
# Fixtures are created when first requested by a test and destroyed based on their scope. At default this is the
# function scope, but fixtures can also be destroyed at the session, class, and module scopes as well to name a few.


# If we use autouse, then all tests will run this fixture
# @pytest.fixture(autouse=True)
# The scope session will run at start up, the yield portion will run when all tests in the session are finished
# @pytest.fixture(scope="session", autouse=True)
@pytest.fixture
def main_set_up():
    print("Launch browser")
    print("Navigate to site B")
    print("Select forms")
    yield
    print("Select cancel")
    print("Close browser")


@pytest.fixture
def banking_set_up():
    print("Launch browser")
    print("Maximize window")
    print("Navigate to site")
    print("Login")
    print("Navigate to account summary")
    yield
    print("Logout")
    print("Close browser")


# Our fixture we will use in Parameters_test.py. This fixture takes in the browser fixture and checks for browser type
# Depending on text used for --browser it will launch a different browser for our session
@pytest.fixture(scope="session")
def browser_setup(browser):
    if browser == "firefox":
        print("Launch Firefox browser")
    elif browser == "chrome":
        print("Launch Chrome browser")
    else:
        print("Launching Edge browser")
    print("Navigate to site C")
    yield
    print("Close browser")


# Add custom options in command line
def pytest_addoption(parser):
    parser.addoption("--browser")


# Helper fixture that returns command line value of --browser option
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
