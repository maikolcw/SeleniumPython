import pytest
import softest

from sampleteststructure.pages.signin_page import SigninPage
from ddt import ddt, data, unpack, file_data
from sampleteststructure.utilities.utils import Utils


# Example of data driven tests, with one test run multiple times with different data
@pytest.mark.usefixtures("expedia_setup")
@ddt
class TestExpediaLogin(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.signin_page = SigninPage(self.driver)

    # Set of data is defined here, then unpacked
    # @data(("johnemail.com",), ("bademail",), ("fake@email",))
    # @unpack
    # def test_bad_login_email(self, email):
    #     error_message_is_visible = self.signin_page.sign_in_with_email_and_return_if_error_message_is_displayed(email)
    #     assert error_message_is_visible is True

    # Takes data from json file
    # @file_data("..\\testdata\\testdata.json")
    # def test_bad_login_email_from_json(self, email):
    #     error_message_is_visible = self.signin_page.sign_in_with_email_and_return_if_error_message_is_displayed(email)
    #     assert error_message_is_visible is True

    # Takes data from yaml file
    @data(*Utils.read_data_from_excel("..\\testdata\\testdata.xlsx", "Sheet1"))
    @unpack
    def test_bad_login_email_from_yaml(self, email):
        error_message_is_visible = self.signin_page.sign_in_with_email_and_return_if_error_message_is_displayed(email)
        assert error_message_is_visible is True
