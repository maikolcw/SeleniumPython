import pytest


# We can use fixtures for tests with multiple arguments using params keyword. The test function will run once for each
# param. Using params is more efficient, instead of writing the same test multiple times but with different data, we
# just need to write it once.

# This fixture has Bob and John for params
@pytest.fixture(params=["Bob", "John"])
# Add request into test argument
def data_for_login(request):
    print("Using % s for login" % request.param)
    # yield marks the Cleanup phase, this is the code we want to run after the tests that use this fixture
    yield
    print("Log out")


# This test uses data_for_login fixture and will run twice, once for Bob and once for John
def test_login(data_for_login):
    print("Logging in successful")


# We can also use mark for tests with multiple arguments
@pytest.mark.parametrize("a, b, result", [(2, 2, 4), (5, 10, 15), (3, 6, 10)])
def test_addition(a, b, result):
    assert a + b == result


# This test utilizes custom command options from conftest.py
def test_navigate_to_about_page(browser_setup):
    print("Navigate to About successful")
