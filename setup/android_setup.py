import pytest
import os

from appium import webdriver

# Framework is missing deviceName, appPackage and appActivity capabilities
apk_name = ''
device_name = ''
app_package = ''
app_activity = ''


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
