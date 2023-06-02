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


# Find search bar element by Name
search_bar = c_driver.find_element(By.NAME, "q")
# Type "Selenium" in search bar
search_bar.send_keys("Selenium")
# Wait to see results
time.sleep(2)
# Hit ENTER on search bar
search_bar.send_keys(Keys.ENTER)
# Wait to see results
time.sleep(2)


# Find search bar element by ID
search_bar = c_driver.find_element(By.ID, "APjFqb")
# Clear search bar
search_bar.clear()
search_bar.send_keys("ID")
time.sleep(2)
search_bar.send_keys(Keys.ENTER)


# Find search bar element by XPath
search_bar = c_driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
search_bar.clear()
search_bar.send_keys("XPath")
time.sleep(2)
search_bar.send_keys(Keys.ENTER)


# Find search bar element by CSS Selector
search_bar = c_driver.find_element(By.CSS_SELECTOR, "#APjFqb")
search_bar.clear()
search_bar.send_keys("CSSSelector")
time.sleep(2)
search_bar.send_keys(Keys.ENTER)
time.sleep(2)


# Find link element by Link Text
css_functions_link = c_driver.find_element(By.LINK_TEXT, "CSS Functions")
# Click element
css_functions_link.click()
time.sleep(2)


# Find link element by Partial Link Text
attr_link = c_driver.find_element(By.PARTIAL_LINK_TEXT, "attr")
attr_link.click()
time.sleep(5)
c_driver.get("https://www.google.com/")
time.sleep(2)


# Find search bar element by Class Name
search_bar = c_driver.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys("Class Name")
time.sleep(2)
search_bar.send_keys(Keys.ENTER)
time.sleep(2)


# Find search bar element by Tag Name
search_bar = c_driver.find_element(By.TAG_NAME, "textarea")
search_bar.clear()
search_bar.send_keys("Tag Name")


# Find more than one element
a_elements = c_driver.find_elements(By.TAG_NAME, "a")
# Prints the text of first ten links
for link in a_elements[:10]:
    print(link.text)
time.sleep(2)


# Tear down
c_driver.close()
