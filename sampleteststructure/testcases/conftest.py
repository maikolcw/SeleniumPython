import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# request is used to deliver web driver to test method that uses this fixture
@pytest.fixture(scope="class")
def expedia_setup(request):
    c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # wait = WebDriverWait(c_driver, 10)
    c_driver.get("https://www.expedia.ca/")
    c_driver.maximize_window()
    # Set the web driver for request
    request.cls.driver = c_driver
    yield
    c_driver.close()
