# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from baseurl import Baseurl

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class social_links_footer(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_social_links_footer(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl)
        wd.find_element_by_css_selector("a.ftr__social-link.ftr__social-link_fb").click()
        wd.get(str(Baseurl.baseurl)
        wd.find_element_by_css_selector("a.ftr__social-link.ftr__social-link_vk").click()
        wd.get(str(Baseurl.baseurl)
        wd.find_element_by_css_selector("a.ftr__social-link.ftr__social-link_tw").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
