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

class authorized_user_can_watch_profiles(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_authorized_user_can_watch_profiles(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "user/1849")
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("111@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("111111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_link_text("Фотографии").click()
        wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Видео']").click()
        wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Мероприятия']").click()
        wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Друзья']").click()
        wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Сообщества']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
