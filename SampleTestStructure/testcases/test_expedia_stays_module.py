import time

import pytest

from SampleTestStructure.pages.home_page import HomePage


@pytest.mark.usefixtures("expedia_setup")
class TestExpediaStaysModule():
    def test_search_bar_text(self):
        home_page = HomePage(self.driver, self.wait)
        text = home_page.return_search_bar_text()
        print(text)
        assert text == "Going to"
        time.sleep(1)
