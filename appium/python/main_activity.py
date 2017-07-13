import os
from time import sleep
import unittest
from appium import webdriver

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MainActivityTests(unittest.TestCase):
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

    def go_to_main(self):
        username_editText = self.driver.find_element_by_id("qa.learningapp:id/editText_username").clear()
        self.driver.set_value(username_editText, 'test@test.com')
        self.driver.hide_keyboard()

        passsword_editText = self.driver.find_element_by_id("qa.learningapp:id/editText_password").clear()
        self.driver.set_value(passsword_editText, '123456')
        self.driver.hide_keyboard()

        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("LOG IN")')
        el.click()
        assert self.driver.find_element_by_android_uiautomator('new UiSelector().text("loading weather...")').is_displayed()

    def test_playing_with_controls(self):
        self.go_to_main()

        # EditText Example by using id
        username_editText = self.driver.find_element_by_id("qa.learningapp:id/editText_username").clear()
        self.driver.set_value(username_editText, 'Abracadabra...')
        self.driver.hide_keyboard()

        # Checkbox example
        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("This is a checkbox")')
        checked = el.get_attribute("checked")
        if checked == 'false':
            el.click()
        sleep(1)
        # Spinner
        spinner = self.driver.find_element_by_id("qa.learningapp:id/spinner_id_342")
        spinner.click()
        large_room = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Large(9+)")')
        large_room.click()

        sleep(1)

        assert True

    def test_playing_with_more_controls(self):
        self.go_to_main()

        # RadioButton1 Example
        el = self.driver.find_element_by_android_uiautomator('new UiSelector().text("female")')
        checked = el.get_attribute("checked")
        if checked == 'false':
            el.click()

        sleep(1)
        # RadioButton 2
        el = self.driver.find_element_by_id("qa.learningapp:id/radio_button_2")
        checked = el.get_attribute("checked")
        if checked == 'false':
            el.click()

        sleep(1)

        assert True


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MainActivityTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
