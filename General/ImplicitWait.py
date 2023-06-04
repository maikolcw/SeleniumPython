from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# It is better to use implicit wait than to use time.sleep, the purpose of time.sleep is mainly to the show results
# Implicit wait, waits for a maximum set of time looking for an element before throwing an error
# It will not wait the maximum time if the element is ready earlier
c_driver.get("https://www.google.com/")
c_driver.maximize_window()

# Here the XPATH is wrong, and an error is thrown
c_driver.find_element(By.XPATH, "//textarea[@id='APjFq']").send_keys("Found")

# If we uncomment the following lines and comment the above, Selenium will wait max 5seconds for element to be found
# Wait max 5 seconds for following
# c_driver.implicitly_wait(5)
# c_driver.find_element(By.XPATH, "//textarea[@id='APjFq']").send_keys("Found")

c_driver.close()
