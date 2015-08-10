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

class static_page_about(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_static_page_about(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl))
        wd.find_element_by_xpath("//div[@class='ftr__nav']//a[.='О проекте']").click()
        if not (len(wd.find_elements_by_xpath("//div[@class='cnt']//h1[.='О проекте']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not ("это информационно-технический портал для работников сферы кино, радио и телевидения" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        if not ("Вступайте в сообщество профессионалов на tvkinoradio.ru!" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
