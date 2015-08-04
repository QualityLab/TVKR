# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class join_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_join_group(self):
        success = True
        wd = self.wd
        wd.get("http://build_2015_7_9_17.build.tvkinoradio.itcreativoff.com/login")
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("z947384@yandex.ru")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("111111")
        wd.find_element_by_id("submit_link").click()
        wd.get("http://build_2015_7_9_17.build.tvkinoradio.itcreativoff.com/group/251")
        wd.find_element_by_link_text("Вступить в группу").click()
        wd.find_element_by_link_text("Сообщества").click()
        if not (len(wd.find_elements_by_link_text("ОНЛАЙН-КОНФЕРЕНЦИИ")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
