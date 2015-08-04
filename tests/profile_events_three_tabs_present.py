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

class profile_events_three_tabs_present(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_profile_events_three_tabs_present(self):
        success = True
        wd = self.wd
        wd.get("http://build_2015_7_22_17.build.tvkinoradio.itcreativoff.com/")
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("123@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("1111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_xpath("//ul[@id='yw2']//a[.='Мероприятия']").click()
        if not (len(wd.find_elements_by_xpath("//div[@class='company-box__section']//a[@href='#tab01']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@class='company-box__section']//a[@href='#tab02']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@class='company-box__section']//a[@href='#tab03']")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
