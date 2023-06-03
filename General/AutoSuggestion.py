from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.google.com/")
c_driver.maximize_window()

# Locate search bar and type "Selenium" for suggestions
search_bar = c_driver.find_element(By.ID, "APjFqb")
search_bar.send_keys("Selenium")
time.sleep(1)

# Select suggestions
search_bar.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
search_bar.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
search_bar.send_keys(Keys.ENTER)
time.sleep(1)

# Locate search bar and type "Selenium" for suggestions
search_bar = c_driver.find_element(By.ID, "APjFqb")
search_bar.clear()
search_bar.send_keys("Selenium")
time.sleep(1)

# Locate list of suggestions
list_elements = c_driver.find_elements(By.XPATH, "(//ul[@role='listbox'])[1]")
time.sleep(1)
# Print out suggestions
for element in list_elements:
    print(element.text)

c_driver.close()
