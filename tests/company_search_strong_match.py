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

class company_search_strong_match(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_(self):
        success = True
        wd = self.wd
        wd.get("http://build_2015_7_8_17.build.tvkinoradio.itcreativoff.com/companies")
        wd.find_element_by_id("keywords").click()
        wd.find_element_by_id("keywords").clear()
        wd.find_element_by_id("keywords").send_keys("3D Media Group")
        wd.find_element_by_id("filter-by-keywords").click()
        wd.find_element_by_link_text("3D Media Group").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
