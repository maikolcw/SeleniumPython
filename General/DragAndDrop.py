from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://jqueryui.com/droppable/")
c_driver.maximize_window()
time.sleep(2)

# Get our locators
iframe_of_interest = c_driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
# Make sure to switch to frame for the inner locators
c_driver.switch_to.frame(iframe_of_interest)
draggable = c_driver.find_element(By.XPATH, "//div[@id='draggable']")
droppable = c_driver.find_element(By.XPATH, "//div[@id='droppable']")

# Create our Action Chains object
action_chains = ActionChains(c_driver)
# Drag and drop our element
action_chains.drag_and_drop(draggable, droppable).perform()
time.sleep(2)

# Drag and drop by offset
action_chains.drag_and_drop_by_offset(draggable, -170, 0).perform()
time.sleep(2)

draggable_location = draggable.location
print("Draggable location property is % s" % draggable_location)
x, y = draggable_location["x"], draggable_location["y"]
print("Draggable coordinates are: x = % s, y = % s" % (x, y))

c_driver.close()
