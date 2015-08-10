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

class pavillions_pavillion_watch(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_pavillions_pavillion_watch(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "pavilions/73")
        wd.find_element_by_xpath("//a[@class='fancybox']").click()
        wd.find_element_by_xpath("//a[@id='fancybox-close']").click()
        wd.find_element_by_link_text("Технические характеристики").click()
        if not (len(wd.find_elements_by_css_selector("div.features__item.line")) != 0):
            success = False
            print("verifyElementPresent failed")
        wd.find_element_by_link_text("Услуги").click()
        if not (len(wd.find_elements_by_css_selector("div.features__item.line")) != 0):
            success = False
            print("verifyElementPresent failed")
        wd.find_element_by_link_text("Расписание").click()
        if not (len(wd.find_elements_by_css_selector("p.pavilion-dates")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
