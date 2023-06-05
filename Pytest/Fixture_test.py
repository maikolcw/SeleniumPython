import pytest


# A test can be broken down into four parts Arrange, Act, Assert, and Cleanup. The Arrange part can be thought of as the
# set up, the Act is the doing like filling in a form, the Assert is to check if the doing is done correctly, and the
# Cleanup is to reset the situation. Fixtures can help us with the Arrange and Cleanup part, and sometimes even the Act.

@pytest.fixture
def set_up():
    print("Launch browser")
    print("Navigate to form")
    # yield marks the Cleanup phase, this is the code we want to run after the tests that use this fixture
    yield
    print("Close browser")


# Before running this test the set_up method will be run
def test_fill_first_name_correctly(set_up):
    print("Proper first name has been entered")


def test_fill_last_name_correctly():
    print("Proper last name has been entered")


def test_fill_phone_number_correctly():
    print("Proper phone number has been entered")
