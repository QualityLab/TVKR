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

class companies_navigation(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_companies_navigation(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl))
        wd.find_element_by_link_text("Компании").click()
        if wd.find_element_by_css_selector("h1.cnt__ttl").text != "Компании":
            success = False
            print("verifyText failed")
        if wd.find_element_by_css_selector("b").text != "Поиск по категориям":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='cnt']//b[.='Новые компании']").text != "Новые компании":
            success = False
            print("verifyText failed")
        if wd.find_element_by_css_selector("p.news_title > b").text != "Новости компаний":
            success = False
            print("verifyText failed")
        wd.find_element_by_id("keywords").click()
        wd.find_element_by_id("keywords").clear()
        wd.find_element_by_id("keywords").send_keys("ООО Корпорация DNK")
        wd.find_element_by_id("filter-by-keywords").click()
        wd.find_element_by_link_text("ООО Корпорация DNK").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
