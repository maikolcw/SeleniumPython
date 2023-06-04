from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
# Some delays with the site
c_driver.maximize_window()
time.sleep(2)

# Switching iframe with locater
c_driver.switch_to.frame(c_driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))

# Switching iframe with ID / Name, this case both use "iframeResult"
# c_driver.switch_to.frame("iframeResult")

# Switching iframe with index
# Switch to first frame within iframe "iframeResult"
c_driver.switch_to.frame(0)

c_driver.find_element(By.XPATH, "//a[@id='signupbtn_topnav']").click()
time.sleep(2)


c_driver.close()
