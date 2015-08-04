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

class articles_navigation(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_articles_navigation(self):
        success = True
        wd = self.wd
        wd.get("http://tvkinoradio.ru/")
        wd.find_element_by_link_text("Статьи").click()
        wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Обзоры']").click()
        wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Мнение']").click()
        wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Слова']").click()
        wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Профессия']").click()
        wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Техника']").click()
        wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Практика']").click()
        wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Репортаж']").click()
        wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Инфографика']").click()
        wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Правила профессии']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
