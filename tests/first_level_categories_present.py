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

class first_level_categories_present(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_(self):
        success = True
        wd = self.wd
        wd.get("http://tvkinoradio.ru/catalog")
        if wd.find_element_by_css_selector("a.catalog__ttl-link").text != "Аудио":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/div/a").text != "Видео":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[1]/div/a").text != "Радиовещание":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[2]/div/a").text != "IT оборудование":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[1]/div/a").text != "Видеомонтаж":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/div/a").text != "Профессиональные носители":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[1]/div/a").text != "Измерительное оборудование":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[2]/div/a").text != "Системы служебной связи":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[1]/div/a").text != "Кабели, разъемы":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[2]/div/a").text != "Осветительное оборудование":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[6]/div[1]/div/a").text != "Оборудование DVB-C и DVB-T":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[6]/div[2]/div/a").text != "Студийная мебель":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[7]/div").text != "Аренда":
            success = False
            print("verifyText failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
