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
