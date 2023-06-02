from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.google.com/")
c_driver.maximize_window()

# Find search bar element by class name and store in variable search_bar
search_bar = c_driver.find_element(By.CLASS_NAME, "gLFyf")
# Type "Selenium" in search bar
search_bar.send_keys("Selenium")
# Wait to see results
time.sleep(2)
# Hit ENTER on search bar
search_bar.send_keys(Keys.ENTER)
# Wait to see results
time.sleep(2)


# Find search bar element by id
search_bar = c_driver.find_element(By.ID, "APjFqb")
# Clear search bar
search_bar.clear()
search_bar.send_keys("Chrome")
time.sleep(2)
search_bar.send_keys(Keys.ENTER)


# Find search bar element by XPath
search_bar = c_driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
search_bar.clear()
search_bar.send_keys("XPath")
time.sleep(2)
search_bar.send_keys(Keys.ENTER)


# Find search bar element by XPath
search_bar = c_driver.find_element(By.CSS_SELECTOR, "#APjFqb")
search_bar.clear()
search_bar.send_keys("CSSSelector")
time.sleep(2)
search_bar.send_keys(Keys.ENTER)
time.sleep(2)

# Tear down
c_driver.close()
