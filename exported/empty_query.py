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

class empty_query(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_empty_query(self):
        success = True
        wd = self.wd
        wd.get("http://tvkinoradio.ru/")
        wd.find_element_by_id("header-search").click()
        wd.find_element_by_id("header-search").clear()
        wd.find_element_by_id("header-search").send_keys()
        wd.find_element_by_css_selector("input.btn_search").click()
        if wd.find_element_by_css_selector("strong.search_result").text != "Вы задали пустой поисковый запрос":
            success = False
            print("verifyText failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
