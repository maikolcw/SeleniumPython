from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# HomePage inherits from BaseDriver to use BaseDriver functions like scroll down
from selenium.webdriver.support.wait import WebDriverWait
from sampleteststructure.base.base_driver import BaseDriver


class AboutPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action_chains = ActionChains(self.driver)

    # Locators
    ABOUT_LOGO = "//a[@href='/home']//img[@alt='Expedia Group Logo']"

    def is_about_logo_visible(self):
        return self.driver.find_element(By.XPATH, self.ABOUT_LOGO).is_displayed()
