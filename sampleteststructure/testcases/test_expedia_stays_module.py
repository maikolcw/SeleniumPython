import time
import datetime

import pytest
import softest

from sampleteststructure.pages.home_page import HomePage


@pytest.mark.usefixtures("expedia_setup")
class TestExpediaStaysModule(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home_page = HomePage(self.driver)

    def test_1_search_bar_text(self):
        text = self.home_page.return_search_bar_text()
        print(text)
        assert text == "Going to"

    def test_2_destination_search_bar_text(self):
        text = self.home_page.return_destination_search_bar_text()
        print(text)
        assert text == "Where are you going?"

    def test_3_travellers_text(self):
        text = self.home_page.return_travellers_text()
        print(text)
        assert text == "1 room, 2 travellers"

    def test_4_default_adult_traveller_count(self):
        text = self.home_page.open_travellers_and_return_default_adult_count()
        print(text)
        assert text == "2"

    def test_5_default_add_adult_traveller(self):
        results = self.home_page.add_adult_traveller_and_return_count()
        print("Initial count: % s and final count: % s" % (results[0], results[1]))
        assert int(results[0]) + 1 == int(results[1])

    def test_6_check_in_disabled_dates(self):
        count = self.home_page.return_number_of_disabled_dates()
        print(count)
        assert datetime.date.today().day - 1 == count
