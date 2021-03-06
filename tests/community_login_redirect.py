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

class community_login_redirect(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_community_login_redirect(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "group/253/members")
        wd.find_element_by_link_text("Фотографии").click()
        wd.get(str(Baseurl.baseurl) + "group/253/members")
        wd.find_element_by_xpath("//ul[@id='yw0']//strong[.=' Видео']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
