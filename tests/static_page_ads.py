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

class static_page_ads(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_static_page_ads(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl))
        wd.find_element_by_link_text("Реклама").click()
        if not (len(wd.find_elements_by_xpath("//div[@class='cnt']//h1[.='Реклама']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not ("Позвонить в редакцию можно по тел. +7 (499) 951-30-32" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
