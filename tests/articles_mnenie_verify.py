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

class articles_mnenie_verify(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_articles_mnenie_verify(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "article/category7")
        if wd.find_element_by_xpath("//div[@class='news news_list']/div[1]/a[@href='/article/category7']").text != "Мнение":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='news news_list']/div[2]/a[@href='/article/category7']").text != "Мнение":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='news news_list']/div[3]/a[@href='/article/category7']").text != "Мнение":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='news news_list']/div[4]/a[@href='/article/category7']").text != "Мнение":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='news news_list']/div[5]/a[@href='/article/category7']").text != "Мнение":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='news news_list']/div[6]/a[@href='/article/category7']").text != "Мнение":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='news news_list']/div[7]/a[@href='/article/category7']").text != "Мнение":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='news news_list']/div[8]/a[@href='/article/category7']").text != "Мнение":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='news news_list']/div[9]/a[@href='/article/category7']").text != "Мнение":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='news news_list']/div[10]/a[@href='/article/category7']").text != "Мнение":
            success = False
            print("verifyText failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
