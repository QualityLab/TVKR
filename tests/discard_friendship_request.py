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

class discard_friendship_request(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_discard_friendship_request(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "login")
        wd.find_element_by_id("UserForm_email").send_keys("123@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").send_keys("1111")
        wd.find_element_by_id("submit_link").click()
        time.sleep(1)
        wd.get(str(Baseurl.baseurl) + "user/user/view?id=2596")
        wd.find_element_by_xpath("//div[@class='profile__meta-status']//span[.='Добавить в друзья']").click()
        time.sleep(3)
        if not (len(wd.find_elements_by_xpath("//a[.='Олеся Подробная']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not ("Заявка отправлена" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        wd.find_element_by_xpath("//a[.='Отменить']").click()
        time.sleep(3)
        if not (len(wd.find_elements_by_xpath("//div[@class='cnt']//a[.='Мои заявки (0)']")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
