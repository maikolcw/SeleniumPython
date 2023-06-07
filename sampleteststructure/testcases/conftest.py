import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
# For Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# For Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# request is used to deliver web driver to test method that uses this fixture
@pytest.fixture(scope="class")
def expedia_setup(request, browser):
    if browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.expedia.ca/")
    driver.maximize_window()
    # Pass webdriver to request class
    request.cls.driver = driver
    yield
    driver.close()


# Add custom options in command line
def pytest_addoption(parser):
    parser.addoption("--browser")


# Helper fixture that returns command line value of --browser option
@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")
