import datetime
import pytest
from sampleteststructure.pages.home_page import HomePage


@pytest.mark.usefixtures("expedia_setup")
class TestExpediaStaysModule():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home_page = HomePage(self.driver)

    # Uncomment for all tests
    # def test_search_bar_text(self):
    #     text = self.home_page.return_search_bar_text()
    #     assert text == "Going to"
    #
    # def test_destination_search_bar_text(self):
    #     text = self.home_page.return_destination_search_bar_text()
    #     assert text == "Where are you going?"
    #
    # def test_travellers_text(self):
    #     text = self.home_page.return_travellers_text()
    #     assert text == "1 room, 2 travellers"

    def test_default_adult_traveller_count(self):
        text = self.home_page.open_travellers_and_return_default_adult_count()
        assert text == "2"

    def test_default_add_adult_traveller(self):
        results = self.home_page.add_adult_traveller_and_return_count()
        assert int(results[0]) + 1 == int(results[1])

    def test_check_in_disabled_dates(self):
        count = self.home_page.return_number_of_checkin_disabled_dates()
        assert datetime.date.today().day - 1 == count
