from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
c_driver.maximize_window()

# Site is using iframes, so we'll need to switch to the iframe element to access its children
time.sleep(1)
c_driver.switch_to.frame("iframeResult")

# Selecting different cars
dropdown_element = c_driver.find_element(By.ID, "cars")
dropdown = Select(dropdown_element)

# Select by index
dropdown.select_by_index(1)
time.sleep(1)

# Select by visible drop down options
dropdown.select_by_visible_text("Opel")
time.sleep(1)

# Select by attribute value
dropdown.select_by_value("audi")
time.sleep(2)

# Navigate to multi select sample
c_driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")
c_driver.switch_to.frame("iframeResult")

# Locate dropdown and select all one at a time
multiselect_element = c_driver.find_element(By.ID, "cars")
multiselect = Select(multiselect_element)
multiselect.select_by_index(0)
time.sleep(1)
multiselect.select_by_visible_text("Saab")
time.sleep(1)
multiselect.select_by_value("opel")
time.sleep(1)
multiselect.select_by_value("audi")
time.sleep(1)

# Deselect one and then deselect all
multiselect.deselect_by_visible_text("Audi")
time.sleep(1)
multiselect.deselect_all()
time.sleep(1)

c_driver.close()
