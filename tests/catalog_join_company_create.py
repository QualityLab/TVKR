# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from baseurl import Baseurl
# перевести на pytest и на юзера, у которого не может появиться тестовой компании

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class catalog_join_company_create(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_catalog_join_company_create(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "catalog")
        wd.find_element_by_link_text("Присоединяйтесь").click()
        wd.find_element_by_id("registration_button").click()
        wd.find_element_by_link_text("Авторизоваться").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("1@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("11111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_link_text("Создать профиль").click()
        if wd.current_url != str(Baseurl.baseurl) + "company/create":
            success = False
            print("verifyCurrentUrl failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
