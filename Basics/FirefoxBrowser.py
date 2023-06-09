from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# We need the corresponding web driver to interface with the browser we want to use
# Or we can use WebDriver Manager

# Selenium v4 syntax
options = Options()
# To get firefox binary
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# Absolute path to your geckodriver.exe
firefox_service = Service("C:\\Users\\Myo\\Documents\\SeleniumWebDrivers\\geckodriver.exe")
firefox_driver = webdriver.Firefox(service=firefox_service, options=options)

firefox_driver.get("https://www.google.com/")
# maximizes browser window
firefox_driver.maximize_window()
# grab and print browser title
print(firefox_driver.title)
# closes current browser tab
firefox_driver.close()
# closes all browser tabs
# firefox_driver.quit()
