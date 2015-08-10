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

class vacancy_create_and_edit(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_vacancy_create_and_edit(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "resume")
        wd.find_element_by_link_text("Разместить вакансию").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("123@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("1111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_id("Vacancy_name").click()
        wd.find_element_by_id("Vacancy_name").clear()
        wd.find_element_by_id("Vacancy_name").send_keys("Создание вакансии")
        if not wd.find_element_by_id("select2-drop-mask").is_selected():
            wd.find_element_by_id("select2-drop-mask").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
