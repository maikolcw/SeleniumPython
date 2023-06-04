from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
c_driver.maximize_window()
time.sleep(2)

# Our element is inside an iframe, so we switch to it first
c_driver.switch_to.frame("iframeResult")

# We locate the try button to click, to activate the alert
try_it_button = c_driver.find_element(By.XPATH, "//button[normalize-space()='Try it']")
try_it_button.click()
# Printing out the alert test
print("The alert message is: % s" % c_driver.switch_to.alert.text)
time.sleep(2)

# Accepting alert
c_driver.switch_to.alert.accept()
time.sleep(2)

try_it_button.click()
time.sleep(2)
# Dismissing alert
c_driver.switch_to.alert.dismiss()
time.sleep(2)

try_it_button.click()
time.sleep(2)
# Sending text to alert input
c_driver.switch_to.alert.send_keys("Selenium is Awesome")
c_driver.switch_to.alert.accept()
time.sleep(2)


c_driver.close()
