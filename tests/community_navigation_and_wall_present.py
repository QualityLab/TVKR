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

class community_navigation_and_wall_present(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_community_navigation_and_wall_present(self):
        success = True
        wd = self.wd
        wd.get("http://build_2015_7_8_17.build.tvkinoradio.itcreativoff.com")
        wd.find_element_by_link_text("Сообщество").click()
        if not (len(wd.find_elements_by_link_text("Виктория Черепанова")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_css_selector("div.comments__holder.comments__holder_txt")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
