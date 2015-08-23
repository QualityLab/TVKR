# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as wait
import time, unittest
from baseurl import Baseurl

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class users_profile_could_be_opened_from_community(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_users_profile_could_be_opened_from_community(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "community")
        wd.find_element_by_link_text("Виктория Черепанова").click()
        wait(wd, 10).until(lambda s: wd.current_url == str(Baseurl.baseurl) + "user/1849")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
