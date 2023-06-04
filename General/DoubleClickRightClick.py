from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://demo.guru99.com/test/simple_context_menu.html")
c_driver.maximize_window()
time.sleep(2)

# Create our Action Chains object
action_chains = ActionChains(c_driver)

# Get our locators
right_click_me_button = c_driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
delete_selection = c_driver.find_element(By.XPATH, "//span[normalize-space()='Delete']")
double_click_me_button = c_driver.find_element(By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']")

# Double click button
action_chains.double_click(double_click_me_button).perform()
time.sleep(2)
# Accept alert
c_driver.switch_to.alert.accept()
time.sleep(2)

# Right click button and click delete
action_chains.context_click(right_click_me_button).click(delete_selection).perform()
time.sleep(2)
c_driver.switch_to.alert.accept()
time.sleep(2)

c_driver.close()