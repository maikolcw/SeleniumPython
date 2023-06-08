from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from sampleteststructure.base.base_driver import BaseDriver
from sampleteststructure.utilities.utils import Utils


# SigninPage contains all locators and functions related to SigninPage
class SigninPage(BaseDriver):
    utils = Utils()
    log = utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action_chains = ActionChains(self.driver)

    # Locators
    EMAIL = "//input[@id='loginFormEmailInput']"
    CONTINUE = "//button[@id='loginFormSubmitButton']"
    EMAIL_ERROR_MESSAGE = "//div[@id='loginFormEmailInput-error']"
    TRY_AGAIN = "//*[@id='app-layer-base']/div/main/div[1]/button"

    SIGN_IN_ADDRESS = "https://www.expedia.ca/login"

    def navigate_to_sign_in(self):
        self.driver.get(self.SIGN_IN_ADDRESS)
        try_again_present = self.driver.find_element(By.XPATH, self.TRY_AGAIN).is_displayed()
        if try_again_present:
            self.driver.find_element(By.XPATH, self.TRY_AGAIN).click()

    def sign_in_with_email_and_return_if_error_message_is_displayed(self, email):
        self.navigate_to_sign_in()
        email_element = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.EMAIL)))
        email_element.send_keys(email)
        self.driver.find_element(By.XPATH, self.CONTINUE).click()
        error_message_is_visible = self.driver.find_element(By.XPATH, self.EMAIL_ERROR_MESSAGE).is_displayed()
        self.log.info("Returned error message is visible: % s" % error_message_is_visible)
        return error_message_is_visible
