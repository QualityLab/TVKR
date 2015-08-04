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

class community_comment(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_community_comment(self):
        success = True
        wd = self.wd
        wd.get("http://build_2015_7_9_17.build.tvkinoradio.itcreativoff.com/community")
        wd.find_element_by_link_text("Комментировать").click()
        wd.find_element_by_link_text("Войдите").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("1@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("11111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_id("Comment_comment_text").click()
        wd.find_element_by_id("Comment_comment_text").click()
        wd.find_element_by_id("Comment_comment_text").clear()
        wd.find_element_by_id("Comment_comment_text").send_keys("Sample comment")
        wd.find_element_by_link_text("Отправить").click()
        if wd.find_element_by_css_selector("div.comments__text > p").text != "Sample comment":
            success = False
            print("verifyText failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
