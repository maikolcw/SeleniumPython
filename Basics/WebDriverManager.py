# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.google.com/")
c_driver.maximize_window()
print(c_driver.title)

f_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
f_driver.get("https://www.mozilla.org/")
f_driver.maximize_window()
print(f_driver.title)

c_driver.quit()
f_driver.quit()