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

class send_message(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_send_message(self):
        success = True
        wd = self.wd
        wd.get("http://build_2015_7_9_17.build.tvkinoradio.itcreativoff.com")
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("1@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("11111")
        wd.find_element_by_id("submit_link").click()
        wd.get("http://build_2015_7_9_17.build.tvkinoradio.itcreativoff.com/user/user/view?id=2391")
        wd.find_element_by_link_text("Отправить сообщение").click()
        wd.find_element_by_id("Message_body").click()
        wd.find_element_by_id("Message_body").clear()
        wd.find_element_by_id("Message_body").send_keys("Sample test message")
        wd.find_element_by_link_text("Отправить").click()
        wd.find_element_by_css_selector("a.account__exit.large-screen").click()
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("z947384@yandex.ru")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("111111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_css_selector("i.ico.ico_comments").click()
        if not ("Sample test message" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
