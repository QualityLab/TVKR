# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from baseurl import Baseurl

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class users_profile_is_visible_from_event(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_users_profile_is_visible_from_event(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "events")
        wd.find_element_by_css_selector("div.event__ttl > a").click()
        time.sleep(2)
        wd.find_element_by_css_selector("a.post__list-person").click()
        wait(wd, 10).until(lambda s: str(Baseurl.baseurl) + "user/" in wd.current_url)
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
