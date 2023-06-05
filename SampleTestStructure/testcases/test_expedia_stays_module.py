import time

import pytest


@pytest.mark.usefixtures("expedia_setup")
class TestExpediaStaysModule():
    def test_elements_present(self):
        print("Placeholder")
        time.sleep(2)


main = TestExpediaStaysModule()
main.test_elements_present()