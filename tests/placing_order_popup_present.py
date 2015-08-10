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

class placing_order_popup_present(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_placing_order_popup_present(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "catalog/video_13/videokameri-i-kamkorderi_128/xdcam_460/product_12700_pxw-x200")
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("1@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("11111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_link_text("Заказать").click()
        if not (len(wd.find_elements_by_xpath("//button[@class='submit-request metrika']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//button[@class='ui-button-cancel']")) != 0):
            success = False
            print("verifyElementPresent failed")
        wd.find_element_by_css_selector("button.submit-request.metrika").click()
        if not (len(wd.find_elements_by_id("request-success")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
