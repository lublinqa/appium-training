from setup.wrappers import AppiumDriver


class HomePage(AppiumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    plus_button = 'op_add'
    equals = 'eq'
    formula = 'formula'

    def check_2_plus_2(self):
        self.tap_digit_button(2)
        self.tap_by_id(self.plus_button)
        self.tap_digit_button(2)
        self.tap_by_id(self.equals)
        # return formula text
