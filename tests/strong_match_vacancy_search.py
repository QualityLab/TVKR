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

class strong_match_vacancy_search(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_strong_match_vacancy_search(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "job")
        wd.find_element_by_id("search_text").click()
        wd.find_element_by_id("search_text").clear()
        wd.find_element_by_id("search_text").send_keys("редактор")
        wd.find_element_by_xpath("//div[@class='tab']//button[.='Найти']").click()
        wd.find_element_by_id("search_text").click()
        wd.find_element_by_id("search_text").clear()
        wd.find_element_by_id("search_text").send_keys()
        if not ("редактор" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
