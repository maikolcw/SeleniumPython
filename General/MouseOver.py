from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://developer.mozilla.org/en-US/")
c_driver.maximize_window()
time.sleep(2)

# Locate plus element that has mouse over event
plus_element = c_driver.find_element(By.XPATH, "//a[normalize-space()='Plus']")

# Create our Action Chains object, takes webdriver as an argument
action_chains = ActionChains(c_driver)

# Move over to plus element and perform this action.
action_chains.move_to_element(plus_element).perform()
time.sleep(2)

# Locate over view element after mouse over
over_view_element = c_driver.find_element(By.XPATH, "//div[normalize-space()='Overview']")

# Show mouse over to over view element and click
action_chains.move_to_element(over_view_element).perform()
time.sleep(2)
over_view_element.click()
time.sleep(2)

# You can chain your actions
action_chains.move_to_element(c_driver.find_element(By.XPATH, "//a[normalize-space()='Plus']"))\
    .move_to_element(c_driver.find_element(By.XPATH, "//div[normalize-space()='Updates']")).click().perform()
time.sleep(2)

c_driver.close()
