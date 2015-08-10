from selenium import webdriver
from .search import SearchHelper
from .companies_search import CompanySearchHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.search = SearchHelper(self)
        self.companies_search = CompanySearchHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def open_companies_page(self):
        wd = self.wd
        wd.get("%s/%s" % (self.base_url, "companies"))

    def type_into(self, web_element, text):
        web_element.click()
        web_element.clear()
        web_element.send_keys(text)

    def destroy(self):
        self.wd.quit()

