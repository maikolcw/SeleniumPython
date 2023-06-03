from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
c_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
c_driver.get("https://www.google.com/")
c_driver.maximize_window()
time.sleep(2)

# Save main tab for access later
main_tab = c_driver.current_window_handle
print(main_tab)

# Create a second tab to blank page and name it secondtab with JavaScript
c_driver.execute_script("window.open('about:blank', 'secondtab');")
# Switch focus to secondtab
c_driver.switch_to.window("secondtab")
time.sleep(2)


c_driver.execute_script("window.open('about:blank', 'thirdtab');")
c_driver.switch_to.window("thirdtab")
# Save all tabs info to a variable
all_tabs = c_driver.window_handles
time.sleep(2)

# Another method to traverse tabs if you don't know tab info
for tab in all_tabs:
    if tab != main_tab:
        c_driver.switch_to.window(tab)
        break
time.sleep(2)

# Switch back to main tab
c_driver.switch_to.window(main_tab)
time.sleep(2)

# Close main tab only
c_driver.close()
time.sleep(2)

# Close all tabs
c_driver.quit()
