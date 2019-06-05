import pytest
import os

from appium import webdriver

apk_name = ''
device_name = 'emulator-5554'
app_package = 'com.android.calculator2'
app_activity = 'com.android.calculator2.Calculator'


@pytest.fixture(scope="class")
def android_set_up(request):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = device_name
    desired_caps['appPackage'] = app_package
    desired_caps['appActivity'] = app_activity

    # app is only mandatory for iOS, android can use appPackage and appActivity caps
    # desired_caps['app'] = apk_name

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
