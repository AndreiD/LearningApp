import os
from time import sleep
import unittest
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginAndroidTests(unittest.TestCase):
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



    # start your test methods with "test_"
    def test_login_ok(self):
        username_editText = self.driver.find_element_by_id("qa.learningapp:id/editText_username").clear()
        self.driver.set_value(username_editText, 'test@test.com')

        passsword_editText = self.driver.find_element_by_id("qa.learningapp:id/editText_password").clear()
        self.driver.set_value(passsword_editText, '123456')
        self.driver.hide_keyboard()

        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("LOG IN")')
        el.click()

        assert self.driver.find_element_by_android_uiautomator('new UiSelector().text("loading weather...")').is_displayed()

    def test_login_not_ok(self):
        username_editText = self.driver.find_element_by_id("qa.learningapp:id/editText_username").clear()
        self.driver.set_value(username_editText, 'invalid@test.com')

        passsword_editText = self.driver.find_element_by_id("qa.learningapp:id/editText_password").clear()
        self.driver.set_value(passsword_editText, 'g23rffae324afds')
        self.driver.hide_keyboard()

        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("LOG IN")')
        el.click()

        try:
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("loading weather...")')
        except NoSuchElementException:
            assert True


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
