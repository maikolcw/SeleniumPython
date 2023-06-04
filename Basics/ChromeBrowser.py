from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# We need the corresponding web driver to interface with the browser we want to use
# Or we can use WebDriver Manager

# Selenium v4 syntax
# Absolute path to your chromedriver.exe
chrome_service = Service("C:\\Users\\Myo\\Documents\\SeleniumWebDrivers\\chromedriver.exe")
chrome_driver = webdriver.Chrome(service=chrome_service)

chrome_driver.get("https://www.google.com/")
# maximizes browser window
chrome_driver.maximize_window()
# grab and print browser title
print(chrome_driver.title)
# closes current browser tab
chrome_driver.close()
# closes all browser tabs
# chrome_driver.quit()
