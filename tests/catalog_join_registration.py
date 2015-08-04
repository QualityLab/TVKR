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

class catalog_join_registration(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_catalog_join_registration(self):
        success = True
        wd = self.wd
        wd.get("http://tvkinoradio.ru/catalog")
        wd.find_element_by_link_text("Присоединяйтесь").click()
        wd.find_element_by_id("registration_button").click()
        wd.find_element_by_xpath("//div[@id='loginPopup']//span[.='Зарегистрироваться']").click()
        if wd.current_url != "http://tvkinoradio.ru/signup?referer=join":
            success = False
            print("verifyCurrentUrl failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
