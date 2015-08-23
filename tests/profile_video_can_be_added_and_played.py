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

class profile_video_can_be_added_and_played(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_profile_video_can_be_added_and_played(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl))
        wd.find_element_by_link_text("Войти").click()
        time.sleep(1)
        wd.find_element_by_id("UserForm_email").send_keys("123@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").send_keys("1111")
        wd.find_element_by_id("submit_link").click()
        time.sleep(1)
        wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Видео']").click()
        time.sleep(1)
        wd.find_element_by_link_text("Добавить альбом").click()
        time.sleep(1)
        wd.find_element_by_id("VideoAlbum_name").send_keys("Test Adding Video")
        wd.find_element_by_css_selector("button.btn.btn_green").click()
        time.sleep(1)
        wd.find_element_by_link_text("Добавить видео").click()
        time.sleep(1)
        wd.find_element_by_id("VideoForm_name").send_keys("New Video")
        wd.find_element_by_id("VideoForm_link").send_keys("https://youtu.be/gKkuY4HuKe4")
        wd.find_element_by_css_selector("button.btn.btn_green").click()
        time.sleep(1)
        wd.find_element_by_css_selector("span.btn_play").click()
        time.sleep(1)
        self.assertTrue(success)
        wd.find_element_by_xpath("//a[@class='ico ico_close jsClosePopup']").click()
        wd.find_element_by_xpath("//div[@class='company-box__section']//a[.='edit']").click()
        time.sleep(1)
        wd.find_element_by_css_selector("div.form__del > label").click()
        wd.find_element_by_css_selector("button.btn.btn_green").click()
        time.sleep(1)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
