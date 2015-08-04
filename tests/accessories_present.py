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

class accessories_present(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_accessories_present(self):
        success = True
        wd = self.wd
        wd.get("http://tvkinoradio.ru/catalog/video_13/videokameri-i-kamkorderi_128/xdcam_460/product_12700_pxw-x200")
        wd.find_element_by_xpath("//ul[@class='tabset']//a[.='Аксессуары']").click()
        wd.find_element_by_link_text("Аккумуляторы для видеокамер DV, HDV, XDCAM EX и др.").click()
        if not (len(wd.find_elements_by_css_selector("div.category__block.line")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
