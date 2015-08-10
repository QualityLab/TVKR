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

class video_album_create_edit_delete(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_video_album_create_edit_delete(self):
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
        wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Видео']").click()
        wd.find_element_by_xpath("//div[@class='btn__holder']//span[.='Добавить альбом']").click()
        wd.find_element_by_id("VideoAlbum_name").click()
        wd.find_element_by_id("VideoAlbum_name").clear()
        wd.find_element_by_id("VideoAlbum_name").send_keys("New album")
        wd.find_element_by_id("VideoAlbum_desc").click()
        wd.find_element_by_id("VideoAlbum_desc").clear()
        wd.find_element_by_id("VideoAlbum_desc").send_keys("Sample description")
        wd.find_element_by_css_selector("button.btn.btn_green").click()
        wd.find_element_by_xpath("//div[@class='company-box__section']//a[.='edit']").click()
        wd.find_element_by_id("VideoAlbum_name").click()
        wd.find_element_by_id("VideoAlbum_name").clear()
        wd.find_element_by_id("VideoAlbum_name").send_keys("New New album")
        wd.find_element_by_id("VideoAlbum_desc").click()
        wd.find_element_by_id("VideoAlbum_desc").clear()
        wd.find_element_by_id("VideoAlbum_desc").send_keys("Новое описание")
        wd.find_element_by_css_selector("button.btn.btn_green").click()
        wd.find_element_by_xpath("//div[@class='company-box__section']//a[.='edit']").click()
        if wd.find_element_by_id("VideoAlbum_desc").text != "Новое описание":
            success = False
            print("verifyText failed")
        wd.find_element_by_css_selector("div.form__del > label").click()
        wd.find_element_by_css_selector("button.btn.btn_green").click()
        if not ("Ни одно видео еще не было загружено." in wd.find_element_by_tag_name("html").text):
            success = False
            print("verifyTextPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
