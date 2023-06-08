import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
# For Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# For Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# request is used to deliver web driver to tests that uses this fixture
@pytest.fixture(autouse=True)
def expedia_setup(request, browser, url):
    # From command line you can select browser type ex. --browser firefox
    # You can add more like Edge, Chromium, and Brave, this is just an example
    if browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.expedia.ca/")
    # We can remove hardcode of URL
    # driver.get(url)
    driver.maximize_window()
    # Pass webdriver to request class
    request.cls.driver = driver
    yield
    driver.close()


# Add custom options in command line
def pytest_addoption(parser):
    parser.addoption("--browser")
    # You can also add more command options like this
    # In this case we can enter our URL from command line
    parser.addoption("--url")


# Helper fixture that returns command line value of --browser option
@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


# Add another command option
@pytest.fixture(scope="class")
def url(request):
    return request.config.getoption("--url")
