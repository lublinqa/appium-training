from setup.wrappers import AppiumDriver


class HomePage(AppiumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    def check_2_plus_2(self):
        pass
