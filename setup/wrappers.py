import pytest


class AppiumDriver:

    def __init__(self, driver):
        self.driver = driver

    def tap_by_id(self, element_id):
        try:
            el = self.driver.find_element_by_id(element_id)
            el.click()
        except:
            pytest.fail('Element {} not found'.format(element_id))

    def tap_digit_button(self, i):
        try:
            self.tap_by_id('digit_{}'.format(i))
        except:
            pytest.fail('Element digit{} not found'.format(i))
