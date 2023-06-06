from selenium.webdriver.common.by import By

# HomePage inherits from BaseDriver to use BaseDriver functions like scroll down
from sampleteststructure.base.base_driver import BaseDriver


class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    SEARCH_BAR = "//button[@aria-label='Going to']"
    DESTINATION_SEARCH_BAR = "//input[@id='location-field-destination']"
    TRAVELLERS_LINK = "//button[normalize-space()='1 room, 2 travellers']"
    TRAVELLERS_ADULT_COUNT_DEFAULT = "//input[@id='adult-input-0']"

    # Attributes
    SEARCH_BAR_ATTRIBUTE = "aria-label"
    DESTINATION_SEARCH_BAR_ATTRIBUTE = "placeholder"
    ADULT_COUNT = "value"

    def return_search_bar_text(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_BAR).get_attribute(self.SEARCH_BAR_ATTRIBUTE)

    def return_destination_search_bar_text(self):
        self.driver.find_element(By.XPATH, self.SEARCH_BAR).click()
        return self.driver.find_element(By.XPATH, self.DESTINATION_SEARCH_BAR) \
            .get_attribute(self.DESTINATION_SEARCH_BAR_ATTRIBUTE)

    def return_travellers_text(self):
        return self.driver.find_element(By.XPATH, self.TRAVELLERS_LINK).text

    def return_adult_count_default(self):
        self.driver.find_element(By.XPATH, self.TRAVELLERS_LINK).click()
        return self.driver.find_element(By.XPATH, self.TRAVELLERS_ADULT_COUNT_DEFAULT).get_attribute(self.ADULT_COUNT)