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

class specs_and_extra_stuff(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_specs_and_extra_stuff(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "catalog/audio_17/mikrofoni_41/radiosistemi_219/product_12878_em-9046-su")
        if not (len(wd.find_elements_by_link_text("Спецификации")) != 0):
            success = False
            print("verifyElementPresent failed")
        wd.find_element_by_link_text("Доп. материалы").click()
        if not (len(wd.find_elements_by_css_selector("a.features__link")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
