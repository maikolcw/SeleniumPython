from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")

# Checking if div element is displayed
time.sleep(2)
div_element = c_driver.find_element(By.XPATH, "//div[@id='myDIV']")
print("Is div element showing: % s" % div_element.is_displayed())

# Toggle hide button to hide div element
c_driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']").click()

# Check if div element is hidden
print("Is div element showing: % s" % div_element.is_displayed())

c_driver.close()