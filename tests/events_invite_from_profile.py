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

class events_invite_from_profile(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_events_invite_from_profile(self):
        success = True
        wd = self.wd
        wd.get("http://tvkinoradio.ru/events")
        wd.find_element_by_xpath("//div[@class='events__block']/div[3]//a[@class='event__img']").click()
        wd.find_element_by_id("join_link").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("111@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("111111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_link_text("Мероприятия").click()
        wd.find_element_by_link_text("Пригласить").click()
        wd.find_element_by_xpath("//label[@for='event2478']").click()
        wd.find_element_by_name("submit_btn").click()
        wd.find_element_by_css_selector("a.account__exit.large-screen").click()
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("1@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("11111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_css_selector("i.ico.ico_message").click()
        if not (len(wd.find_elements_by_xpath("//div[@class='notification__holder']/div[1]//a[.='Олеся Подробная']")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
