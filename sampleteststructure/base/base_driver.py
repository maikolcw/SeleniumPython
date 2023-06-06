
# Contains our base functions which can be used by all classes in pages package
class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self, height):
        self.driver.execute_script("window.scrollTo(0, % d)" % height)
