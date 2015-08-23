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

class add_friend_flow(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_friend_flow(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "login")
        wd.find_element_by_id("UserForm_email").send_keys("123@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").send_keys("1111")
        wd.find_element_by_id("submit_link").click()
        wd.get(str(Baseurl.baseurl) + "user/user/view?id=2596")
        wd.find_element_by_xpath("//div[@class='profile__meta-status']//span[.='Добавить в друзья']").click()
        if not (len(wd.find_elements_by_xpath("//a[.='Олеся Подробная']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not ("Заявка отправлена" in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        if not (len(wd.find_elements_by_xpath("//a[.='Отменить']")) != 0):
            success = False
            print("verifyElementPresent failed")
        wd.find_element_by_css_selector("a.account__exit.large-screen").click()
        wd.get(str(Baseurl.baseurl) + "login")
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("111@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("111111")
        wd.find_element_by_id("submit_link").click()
        wd.get(str(Baseurl.baseurl) + "user/friends/list/#tab02")
        if not (len(wd.find_elements_by_xpath("//strong/a[@href=\"/user/2767\"]")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
        wd.find_element_by_css_selector("a.account__exit.large-screen").click() #возвращаем систему в исходное состояние - отменяем заявку
        wd.get(str(Baseurl.baseurl) + "login")
        wd.find_element_by_id("UserForm_email").send_keys("123@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").send_keys("1111")
        wd.find_element_by_id("submit_link").click()
        wd.get(str(Baseurl.baseurl) + "user/friends/list#tab03")
        wd.find_element_by_xpath("//a[.='Отменить']").click()
        time.sleep(2)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
