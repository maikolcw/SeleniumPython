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
    TRAVELLERS_ADULT_COUNT_DEFAULT_INCREASE_BUTTON = "//div[@class='uitk-layout-flex " \
                                                     "uitk-layout-flex-align-items-center " \
                                                     "uitk-layout-flex-justify-content-space-between uitk-step-input " \
                                                     "adultStepInput uitk-step-input-mounted']//button[2]//span[1] "
    TRAVELLERS_DONE_BUTTON = "//button[normalize-space()='Done']"

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

    def open_travellers_and_return_default_adult_count(self):
        self.driver.find_element(By.XPATH, self.TRAVELLERS_LINK).click()
        return self.driver.find_element(By.XPATH, self.TRAVELLERS_ADULT_COUNT_DEFAULT).get_attribute(self.ADULT_COUNT)

    def return_default_adult_count(self):
        return self.driver.find_element(By.XPATH, self.TRAVELLERS_ADULT_COUNT_DEFAULT).get_attribute(self.ADULT_COUNT)

    def close_travellers_drop_down(self):
        self.driver.find_element(By.XPATH, self.TRAVELLERS_DONE_BUTTON).click()

    def click_default_adult_traveller_add_button(self):
        self.driver.find_element(By.XPATH, self.TRAVELLERS_ADULT_COUNT_DEFAULT_INCREASE_BUTTON).click()