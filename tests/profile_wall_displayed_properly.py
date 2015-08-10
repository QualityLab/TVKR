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

class profile_wall_displayed_properly(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_profile_wall_displayed_properly(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl))
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("123@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("1111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Фотографии']").click()
        wd.find_element_by_xpath("//div[@class='btn__holder']//span[.='Добавить альбом']").click()
        wd.find_element_by_id("Album_name").click()
        wd.find_element_by_id("Album_name").clear()
        wd.find_element_by_id("Album_name").send_keys("New album")
        wd.find_element_by_id("Album_body").click()
        wd.find_element_by_id("Album_body").clear()
        wd.find_element_by_id("Album_body").send_keys("Sample description")
        wd.find_element_by_name("yt0").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
