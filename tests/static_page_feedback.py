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

class static_page_feedback(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_static_page_feedback(self):
        success = True
        wd = self.wd
        wd.get("http://build_2015_7_28_17.build.tvkinoradio.itcreativoff.com")
        wd.find_element_by_xpath("//div[@class='ftr__nav']//a[.='Обратная связь']").click()
        if not (len(wd.find_elements_by_xpath("//div[@class='cnt']//h1[.='Связаться с нами']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not ("Если вы хотите предложить сотрудничество, сообщить о новости или теме для" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        if not (len(wd.find_elements_by_id("Feedback_username")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_id("Feedback_contacts")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_id("Feedback_message")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_name("yt0")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
