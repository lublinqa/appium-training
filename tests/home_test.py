import pytest
import unittest

from pages.home_page import HomePage
from setup.android_setup import android_set_up


@pytest.mark.usefixtures('android_set_up')
class HomeTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, android_set_up):
        self.hp = HomePage(self.driver)

    # TODO: assertions
    def test_home(self):
        self.hp.check_2_plus_2()
