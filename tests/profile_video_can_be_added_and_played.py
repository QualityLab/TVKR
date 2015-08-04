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

class profile_video_can_be_added_and_played(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_profile_video_can_be_added_and_played(self):
        success = True
        wd = self.wd
        wd.get("http://build_2015_7_22_17.build.tvkinoradio.itcreativoff.com/")
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("123@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("1111")
        wd.find_element_by_id("submit_link").click()
        wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Видео']").click()
        wd.find_element_by_link_text("Добавить альбом").click()
        wd.find_element_by_id("VideoAlbum_name").click()
        wd.find_element_by_id("VideoAlbum_name").clear()
        wd.find_element_by_id("VideoAlbum_name").send_keys("Test Adding Video")
        wd.find_element_by_css_selector("button.btn.btn_green").click()
        wd.find_element_by_link_text("Добавить видео").click()
        wd.find_element_by_id("VideoForm_name").click()
        wd.find_element_by_id("VideoForm_name").clear()
        wd.find_element_by_id("VideoForm_name").send_keys("New Video")
        wd.find_element_by_id("VideoForm_link").click()
        wd.find_element_by_id("VideoForm_link").clear()
        wd.find_element_by_id("VideoForm_link").send_keys("https://youtu.be/gKkuY4HuKe4")
        wd.find_element_by_css_selector("button.btn.btn_green").click()
        wd.find_element_by_css_selector("span.btn_play").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
