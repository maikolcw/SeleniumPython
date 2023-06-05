import pytest


# Defining fixtures in every test file can quickly get tedious and reduce code readability. An alternative is to put our
# fixtures in conftest.py where we can access the functions from every test file.
# Fixtures are created when first requested by a test and destroyed based on their scope. At default this is the
# function scope, but fixtures can also be destroyed at the session, class, and module scopes as well to name a few.


# If we use autouse, then all tests will run this fixture
# @pytest.fixture(autouse=True)
# The scope session will run at start up, the yield portion will run when all tests in the session are finished
# @pytest.fixture(scope="session", autouse=True)
@pytest.fixture(autouse=True)
def main_set_up():
    print("Launch browser")
    print("Navigate to site B")
    print("Select forms")
    # yield marks the Cleanup phase, this is the code we want to run after the tests that use this fixture
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
