from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.google.com/")

# Maximize window without blocking OS toolbars
c_driver.maximize_window()
time.sleep(2)

# Maximize browser fully
c_driver.fullscreen_window()
time.sleep(2)

# Minimize browser
c_driver.minimize_window()
time.sleep(2)
c_driver.maximize_window()
time.sleep(2)

# Prints current URL
print("Printing URL: % s" % c_driver.current_url)
# Prints title
print("Printing title: % s" % c_driver.title)

# Refreshes page
c_driver.refresh()
time.sleep(2)
search_bar = c_driver.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys("Create navigation history")
search_bar.send_keys(Keys.ENTER)
time.sleep(2)

# Navigate to previous page
c_driver.back()
time.sleep(2)

# Navigate forward
c_driver.forward()
time.sleep(2)

c_driver.quit()
