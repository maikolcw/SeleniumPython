from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://twitter.com/i/flow/login")
c_driver.maximize_window()
time.sleep(2)

# Different ways of taking screenshots for error messages
# Find an element and take a screenshot of the element
sign_in = c_driver.find_element(By.XPATH, "(//div[@class='css-1dbjc4n r-14lw9ot r-6koalj r-16y2uox r-1wbh5a2'])[1]")
sign_in.screenshot(".\\Results\\signin.png")

# Take screenshot of the browser before warning message
c_driver.get_screenshot_as_file(".\\Results\\signin_nowarning.png")

# Take screenshot of the browser after clicking next button
next_button = c_driver.find_element(By.XPATH, "//span[contains(text(),'Next')]")
next_button.click()
c_driver.save_screenshot(".\\Results\\signin_warning.png")

c_driver.close()
