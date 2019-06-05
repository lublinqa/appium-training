# LublinQA Appium Training

### Prerequisites:
- [Python3.7](https://www.python.org/downloads/)
- [Appium Desktop](https://github.com/appium/appium-desktop/releases/)
- [pyTest](https://docs.pytest.org/en/latest/getting-started.html)
- [Allure](https://pypi.org/project/allure-pytest/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)



### To run the project:
1. `git clone https://github.com/lublinqa/appium-training.git appium-training`
2. `mkdir appium-training`
3. `virtualenv venv`
4. `source venv/bin/activate`
5. `pip3 install -r requirements.txt`
6. Connect a device
7. Set the capabilities to your device in android_setup.py (device, app and remote url)
8. Install appium desktop
9. Start Appium server to match remote url.
10. `python3 -m pytest` to run the suite