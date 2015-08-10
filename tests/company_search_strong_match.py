# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .baseurl import Baseurl
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class company_search_strong_match(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()

    def test_strong(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "companies")
        company_links = wd.find_elements_by_link_text("3D Media Group")
        wd.find_element_by_id("keywords").click()
        wd.find_element_by_id("keywords").clear()
        wd.find_element_by_id("keywords").send_keys("3D Media Group")
        wd.find_element_by_id("filter-by-keywords").click()
        if len(company_links) > 0:
            WebDriverWait(wd, 30).until(EC.staleness_of(company_links[0]))
        wd.find_element_by_link_text("3D Media Group").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
