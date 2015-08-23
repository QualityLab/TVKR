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

class join_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(20)
    
    def test_join_group(self):
        success = True
        wd = self.wd
        actions = ActionChains(wd)
        wd.get(str(Baseurl.baseurl) + "login")
        wd.find_element_by_id("UserForm_email").send_keys("z947384@yandex.ru")
        wd.find_element_by_id("UserForm_password").send_keys("111111")
        wd.find_element_by_id("submit_link").click()
        wd.get(str(Baseurl.baseurl) + "group/251")
        wd.find_element_by_link_text("Вступить в группу").click()
        wd.find_element_by_link_text("Сообщества").click()
        time.sleep(3)
        if not (len(wd.find_elements_by_link_text("ОНЛАЙН-КОНФЕРЕНЦИИ")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
        wd.get(str(Baseurl.baseurl) + "group/251/leave") #восстанавливаем исходное состояние - выходим из группы
        
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
