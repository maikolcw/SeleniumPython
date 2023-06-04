import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# When certain elements in the dom requires waiting time, we can use explicit wait
# Which checks the element for a condition and max time to check for this condition

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.ebay.ca/")
c_driver.maximize_window()

# Explicit wait for max 10 seconds
wait = WebDriverWait(c_driver, 10)
# Wait for element, expected condition is element has to be clickable For more conditions go here
# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
# ?highlight=expected
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@id='gh-shop-a']"))).click()
time.sleep(2)


c_driver.close()
