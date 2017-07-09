import json
import os
from time import sleep
import unittest
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class FunkyTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            'C:\\workspace\\LearningApp\\app\\build\\outputs\\apk\\debug\\app-debug.apk'
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    # example sending app to background ~~~
    def test_app_to_background(self):
        self.driver.background_app(1)
        assert True

    # check app is installed
    def test_app_is_installed(self):
        self.assertFalse(self.driver.is_app_installed('sdfdsfsdfsdf'))
        self.assertTrue(self.driver.is_app_installed('qa.learningapp'))

    # retrieve file
    def test_retrive_file(self):
        data = self.driver.pull_file('data/local/tmp/strings.json')
        xstrings = json.loads(data.decode('base64', 'strict'))
        print("Strings are: " + str(xstrings))

    # lock
    def test_lock(self):
        print("device is now locked...")
        self.driver.lock(2)
        sleep(1)

        # example custom adb command
        os.popen('adb shell input keyevent 82')  # unlock device

        # adb shell input keyevent 26 #Pressing the lock button
        # adb shell input touchscreen swipe 930 880 930 380 #Swipe UP
        # adb shell input text XXXX #Entering your passcode
        # adb shell input keyevent 66 #Pressing Enter

        assert True


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FunkyTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
