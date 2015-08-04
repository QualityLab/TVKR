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

class several_brands_filter(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_several_brands_filter(self):
        success = True
        wd = self.wd
        wd.get("http://build_r_2015_7_30.build.tvkinoradio.itcreativoff.com/catalog/video_13/videokameri-i-kamkorderi_128/")
        wd.find_element_by_xpath("//label[@for='Brand_25']").click()
        wd.find_element_by_xpath("//label[@for='Brand_49']").click()
        wd.find_element_by_xpath("//label[@for='Brand_41']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
