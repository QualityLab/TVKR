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

class companies_search_partly_match(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_companies_search_partly_match(self):
        success = True
        wd = self.wd
        wd.get("http://build_2015_7_8_17.build.tvkinoradio.itcreativoff.com/companies")
        wd.find_element_by_id("keywords").click()
        wd.find_element_by_id("keywords").clear()
        wd.find_element_by_id("keywords").send_keys("русские студии")
        wd.find_element_by_id("filter-by-keywords").click()
        wd.find_element_by_link_text("Всемирные Русские Студии - Санкт-Петербург").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
