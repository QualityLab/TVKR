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

class single_event_displayed_properly(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_single_event_displayed_properly(self):
        success = True
        wd = self.wd
        wd.get("http://tvkinoradio.ru/events")
        wd.find_element_by_css_selector("div.event__ttl > a").click()
        if not (len(wd.find_elements_by_xpath("//div[@class='post__img']/a/img")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//li[@class='post__entry_date']/p[1]")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//li[@class='post__entry_date']/p[2]")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_id("join_link")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_css_selector("li.post__entry_address > p")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_css_selector("div.post__info.line")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_css_selector("h3.post__section-ttl")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
