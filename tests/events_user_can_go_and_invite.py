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

class events_user_can_go_and_invite(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_events_user_can_go_and_invite(self):
        success = True
        wd = self.wd
        wd.get("http://tvkinoradio.ru/events")
        wd.find_element_by_css_selector("div.event__ttl > a").click()
        wd.find_element_by_id("join_link").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("1@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("11111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_id("invite_friends").click()
        wd.find_element_by_xpath("//label[@for='event2596']").click()
        wd.find_element_by_name("submit_btn").click()
        wd.find_element_by_css_selector("a.account__exit.large-screen").click()
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("111@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("111111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_css_selector("i.ico.ico_message").click()
        if wd.find_element_by_xpath("//div[@class='notification__holder']//div[@class='notification__cnt']//a[@href='/user/2478']").text != "Ирина Васюкова":
            success = False
            print("verifyText failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
