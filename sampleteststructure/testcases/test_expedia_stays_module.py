import pytest

from sampleteststructure.pages.home_page import HomePage


@pytest.mark.usefixtures("expedia_setup")
class TestExpediaStaysModule():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.home_page = HomePage(self.driver)

    def test_search_bar_text(self):
        text = self.home_page.return_search_bar_text()
        print(text)
        assert text == "Going to"

    def test_destination_search_bar_text(self):
        text = self.home_page.return_destination_search_bar_text()
        print(text)
        assert text == "Where are you going?"

    def test_travellers_text(self):
        text = self.home_page.return_travellers_text()
        print(text)
        assert text == "1 room, 2 travellers"

    def test_default_adult_traveller_count(self):
        text = self.home_page.open_travellers_and_return_default_adult_count()
        self.home_page.close_travellers_drop_down()
        print(text)
        assert text == "2"

    def test_default_add_adult_traveller(self):
        initial_count = self.home_page.open_travellers_and_return_default_adult_count()
        self.home_page.click_default_adult_traveller_add_button()
        final_count = self.home_page.return_default_adult_count()
        print("% s + 1 == % s" % (initial_count, final_count))
        assert int(initial_count) + 1 == int(final_count)
