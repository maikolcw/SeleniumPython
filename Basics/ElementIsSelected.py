from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.w3schools.com/howto/howto_css_custom_checkbox.asp")
c_driver.maximize_window()

# Find default checkbox two, check it, and check if selected
time.sleep(2)
default_checkbox_two = c_driver.find_element(By.XPATH, "//div[@id='belowtopnav']//input[2]")
print("Is default checkbox two selected: % s" % default_checkbox_two.is_selected())
default_checkbox_two.click()
print("Is default checkbox two selected now: % s" % default_checkbox_two.is_selected())

# Find default radio button and check if selected
default_radio_button_two = c_driver.find_element(By.XPATH, "//div[@id='belowtopnav']//input[2]")
print("Is default radio button two selected: % s" % default_radio_button_two.is_selected())
time.sleep(2)

c_driver.close()