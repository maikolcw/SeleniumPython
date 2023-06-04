import time

from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# When we want to specify the checking frequency for explicit wait and exceptions to ignore,
# we can use fluent wait

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.ebay.ca/")
c_driver.maximize_window()

# Fluent wait for max 10 seconds, frequency set to 2, ignore not visible and selectable exceptions
wait = WebDriverWait(c_driver, 10, poll_frequency=2, ignored_exceptions=[ElementNotVisibleException,
                                                                         ElementNotSelectableException])
# Wait for element, expected condition is element has to be clickable For more conditions go here
# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
# ?highlight=expected
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@id='gh-shop-a']"))).click()
time.sleep(2)


c_driver.close()
