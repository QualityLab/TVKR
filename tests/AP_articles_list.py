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

class AP_articles_list(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_AP_articles_list(self):
        success = True
        wd = self.wd
        wd.get("http://build_2015_7_28_17.build.tvkinoradio.itcreativoff.com")
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("testtvkinoradio@gmail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("test12")
        wd.find_element_by_id("submit_link").click()
        wd.get("http://build_2015_7_28_17.build.tvkinoradio.itcreativoff.com/admin/article/index")
        if not (len(wd.find_elements_by_xpath("//h1[.='Статьи']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c0']//a[.='#']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c1']//a[.='Название']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@id='article-grid']//th[.='Изображение']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c3']//a[.='Категория']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c4']//a[.='Опубликована']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@id='article-grid']//th[.='Автор']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c6']//a[.='Состояние']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c7']//a[.='Просмотры']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c8']//a[.='Читатели']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c9']/a[@href=\"/admin/article/index?Article_sort=countVkLike\"]")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c10']/a[@href=\"/admin/article/index?Article_sort=countFbLike\"]")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c11']/a[@href=\"/admin/article/index?Article_sort=countTwLike\"]")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//th[@id='article-grid_c12']/a[@href=\"/admin/article/index?Article_sort=countGpLike\"]")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_css_selector("#Article_id")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_css_selector("#Article_name")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_css_selector("#Article_category_id")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_id("Article_published_at")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_id("Article_status")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//tr[@class='odd']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//tr[@class='even']")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
