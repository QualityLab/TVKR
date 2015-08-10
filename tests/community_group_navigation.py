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

class community_group_navigation(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_community_group_navigation(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "community")
        wd.find_element_by_id("search_text").click()
        wd.find_element_by_id("search_text").clear()
        wd.find_element_by_id("search_text").send_keys("конкурсы")
        wd.find_element_by_xpath("//div[@class='form_row']//button[.='Найти']").click()
        wd.find_element_by_link_text("Конкурсы, акции и подарки").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
