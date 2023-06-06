from selenium.webdriver.common.by import By

from SampleTestStructure.base.base_driver import BaseDriver


# HomePage inherits from BaseDriver to use BaseDriver functions like scroll down
class HomePage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    def return_search_bar_text(self):
        return self.driver.find_element(By.XPATH, "//button[@aria-label='Going to']").get_attribute("aria-label")
