from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from sampleteststructure.base.base_driver import BaseDriver


# HomePage contains all locators and functions related to HomePage
# HomePage inherits from BaseDriver to use BaseDriver functions like scroll down
class HomePage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action_chains = ActionChains(self.driver)

    # Locators
    SEARCH_BAR = "//button[@aria-label='Going to']"
    DESTINATION_SEARCH_BAR = "//input[@id='location-field-destination']"
    TRAVELLERS_LINK = "//div[@id='adaptive-menu']"
    TRAVELLERS_ADULT_COUNT_DEFAULT = "//input[@id='adult-input-0']"
    TRAVELLERS_ADULT_COUNT_DEFAULT_INCREASE_BUTTON = "//div[@class='uitk-layout-flex " \
                                                     "uitk-layout-flex-align-items-center " \
                                                     "uitk-layout-flex-justify-content-space-between uitk-step-input " \
                                                     "adultStepInput uitk-step-input-mounted']//button[2]//span[1] "
    TRAVELLERS_DONE_BUTTON = "//button[normalize-space()='Done']"
    CHECK_IN_BUTTON = "//button[@id='d1-btn']"
    CHECK_IN_DISABLED_DATES = "//div[@class='uitk-calendar']//div[1]//table[1]//button"
    ABOUT = "//a[normalize-space()='About']"

    # Attributes
    SEARCH_BAR_ATTRIBUTE = "aria-label"
    DESTINATION_SEARCH_BAR_ATTRIBUTE = "placeholder"
    ADULT_COUNT = "value"
    DATE_STATUS = "class"

    def return_search_bar_text(self):
        text = self.driver.find_element(By.XPATH, self.SEARCH_BAR).get_attribute(self.SEARCH_BAR_ATTRIBUTE)
        self.log.info("Returned search bar text is: % s" % text)
        return text

    def click_search_bar(self):
        self.driver.find_element(By.XPATH, self.SEARCH_BAR).click()

    def return_destination_search_bar_text(self):
        self.click_search_bar()
        text = self.driver.find_element(By.XPATH, self.DESTINATION_SEARCH_BAR) \
            .get_attribute(self.DESTINATION_SEARCH_BAR_ATTRIBUTE)
        self.log.info("Returned destination search bar text is: % s" % text)
        self.action_chains.send_keys(Keys.ESCAPE).perform()
        return text

    def return_travellers_text(self):
        text = self.driver.find_element(By.XPATH, self.TRAVELLERS_LINK).text
        self.log.info("Returned travellers text is: % s" % text)
        return text

    def open_travellers_and_return_default_adult_count(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.TRAVELLERS_LINK))).click()
        text = self.driver.find_element(By.XPATH, self.TRAVELLERS_ADULT_COUNT_DEFAULT).get_attribute(self.ADULT_COUNT)
        self.action_chains.send_keys(Keys.ESCAPE).perform()
        self.log.info("Returned default adult count is: % s" % text)
        return text

    def click_travellers_link(self):
        self.driver.find_element(By.XPATH, self.TRAVELLERS_LINK).click()

    def return_default_adult_count(self):
        return self.driver.find_element(By.XPATH, self.TRAVELLERS_ADULT_COUNT_DEFAULT).get_attribute(self.ADULT_COUNT)

    def close_travellers_drop_down(self):
        self.driver.find_element(By.XPATH, self.TRAVELLERS_DONE_BUTTON).click()

    def click_default_adult_traveller_add_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.
                                                                     TRAVELLERS_ADULT_COUNT_DEFAULT_INCREASE_BUTTON))). \
            click()

    def add_adult_traveller_and_return_count(self):
        self.click_travellers_link()
        initial_count = self.return_default_adult_count()
        self.click_default_adult_traveller_add_button()
        final_count = self.return_default_adult_count()
        self.action_chains.send_keys(Keys.ESCAPE).perform()
        self.log.info("Returned initial count: % s and final count: % s" % (initial_count, final_count))
        return [initial_count, final_count]

    def click_check_in_date(self):
        self.driver.find_element(By.XPATH, self.CHECK_IN_BUTTON).click()

    def get_check_in_dates(self):
        list_of_elements = self.wait.until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, self.CHECK_IN_DISABLED_DATES)))
        return list_of_elements

    def return_number_of_checkin_disabled_dates(self):
        self.click_check_in_date()
        list_of_elements = self.get_check_in_dates()
        disabled_date_count = 0
        for element in list_of_elements:
            if "disabled" in element.get_attribute(self.DATE_STATUS):
                disabled_date_count += 1
        self.action_chains.send_keys(Keys.ESCAPE).perform()
        self.log.info("Returned number of checkin disabled dates is: % d" % disabled_date_count)
        return disabled_date_count

    def click_about_link(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.ABOUT))).click()

    def scroll_down_and_click_about_link(self):
        self.scroll_down(2500)
        self.click_about_link()
