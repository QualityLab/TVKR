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

class rent_sale_filters(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_rent_sale_filters(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "catalog/video_13/videokameri-i-kamkorderi_128/")
        wd.find_element_by_xpath("//label[.='Только аренда']").click()
        if wd.current_url != str(Baseurl.baseurl) + "catalog/video_13/videokameri-i-kamkorderi_128/?offerType=rent":
            success = False
            print("verifyCurrentUrl failed")
        wait(wd, 10).until(lambda s: "Средняя цена аренды" in wd.find_element_by_xpath("//div[@class='reviews__price']").text)
        wd.find_element_by_xpath("//label[.='Только продажа']").click()
        if wd.current_url != str(Baseurl.baseurl) + "catalog/video_13/videokameri-i-kamkorderi_128/?offerType=sale":
            success = False
            print("verifyCurrentUrl failed")
        wait(wd, 10).until(lambda s: "Средняя цена продажи" in wd.find_element_by_xpath("//div[@class='reviews__price']").text)
        wd.find_element_by_xpath("//label[.='Весь каталог']").click()
        if wd.current_url != str(Baseurl.baseurl) + "catalog/video_13/videokameri-i-kamkorderi_128/":
            success = False
            print("verifyCurrentUrl failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
