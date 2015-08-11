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
class articles_navigation(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
	@pytest.mark.parametrize("locator,url", [
	    ("//ul[@id='yw0']//a[.='Обзоры']", "article/category2"),
	    ("//ul[@id='yw0']//a[.='Мнение']", "article/category7"),
    ])
	def test_articles_navigation(self, locator, url):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "/article")
		wd.find_element_by_xpath(str(locator)).click()
		assert getCurrentUrl() == str(Baseurl.baseurl) + url
    	self.assertTrue(success)
	def tearDown(self):
        self.wd.quit()
if __name__ == '__main__':
    unittest.main()		