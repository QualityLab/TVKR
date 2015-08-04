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

class brands_navigation_plus_photo_video(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_brands_navigation_plus_photo_video(self):
        success = True
        wd = self.wd
        wd.get("http://tvkinoradio.ru/")
        wd.find_element_by_link_text("Оборудование").click()
        wd.find_element_by_link_text("Производители").click()
        wd.find_element_by_xpath("//a[@href='/catalog/productBrand?mode=logos']").click()
        wd.find_element_by_xpath("//a[@title='Fujinon']").click()
        wd.find_element_by_css_selector("img.fbg-list-image.visual__list-image").click()
        wd.find_element_by_id("fancybox-close").click()
        wd.find_element_by_link_text("play").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
