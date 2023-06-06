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
