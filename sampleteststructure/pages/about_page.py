from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from sampleteststructure.base.base_driver import BaseDriver
from sampleteststructure.utilities.utils import Utils


# AboutPage contains all locators and functions related to AboutPage
class AboutPage(BaseDriver):
    utils = Utils()
    log = utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action_chains = ActionChains(self.driver)

    # Locators
    ABOUT_LOGO = "//a[@href='/home']//img[@alt='Expedia Group Logo']"

    def is_about_logo_visible(self):
        boolean = self.driver.find_element(By.XPATH, self.ABOUT_LOGO).is_displayed()
        self.log.info("Returned about logo is visible: % s" % boolean)
        return boolean
