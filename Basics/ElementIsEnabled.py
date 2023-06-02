from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.expedia.ca/login")

# Checking if Next button is enabled
time.sleep(2)
continue_button = c_driver.find_element(By.XPATH, "//button[@id='loginFormSubmitButton']")
print("Is continue button enabled: % s" % continue_button.is_enabled())

# Insert some dummy value to change state of continue button
text_input = c_driver.find_element(By.XPATH, "//input[@id='loginFormEmailInput']")
text_input.send_keys("Test")
time.sleep(2)
print("Is continue button enable: % s" % continue_button.is_enabled())

c_driver.close()