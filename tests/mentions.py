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

class mentions(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_mentions(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "catalog/audio_17/mikrofoni_41/studijnie-mikrofoni_881/lentochnie_1069/product_14783_ntr")
        wd.find_element_by_css_selector("a.tabset__link.comments__count").click()
        if not ("Интересный микрофон! Давно его ждали" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        if wd.find_element_by_id("add-review-link").text != "Оставьте свой отзыв":
            success = False
            print("verifyText failed")
        wd.find_element_by_id("add-review-link").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("1@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("11111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_css_selector("a.tabset__link.comments__count").click()
        if not (len(wd.find_elements_by_xpath("//div[@class='estimate__comment']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@class='form__bottom']/button")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
