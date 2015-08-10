# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from .baseurl import Baseurl

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class profile_groups_displayed_properly(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_profile_groups_displayed_properly(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl))
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("z947384@yandex.ru")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("111111")
        wd.find_element_by_id("submit_link").click()
        wd.get(str(Baseurl.baseurl) + "group/my/#tab01")
        if not (len(wd.find_elements_by_xpath("//div[@id='tab01']//a[.='Барахолка']")) !=0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@id='tab01']//a[.='Копирайтеры в медиа']")) !=0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@id='tab01']/div/div[1]//img")) !=0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@id='tab01']/div/div[2]//img")) !=0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
