import time
import datetime

import pytest

from sampleteststructure.pages.home_page import HomePage
from sampleteststructure.pages.about_page import AboutPage


@pytest.mark.usefixtures("expedia_setup")
class TestExpediaFooter():

    # Set up page objects
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home_page = HomePage(self.driver)
        self.about_page = AboutPage(self.driver)

    def test_1_check_about_logo_is_present(self):
        self.home_page.scroll_down(2500)
        self.home_page.click_about_link()
        time.sleep(2)
        boolean = self.about_page.is_about_logo_visible()
        print(boolean)
        time.sleep(2)
