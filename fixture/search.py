# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait as wait
import re

class SearchHelper:

    def __init__(self, app):
        self.app = app

    def find(self, query):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.type_into(wd.find_element_by_id("header-search"), query)
        wd.find_element_by_css_selector("input.btn_search").click()

    def wait_results(self):
        wd = self.app.wd
        wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("h1.cnt__ttl").text == "Результаты поиска")

    def get_result_message(self):
        wd = self.app.wd
        self.wait_results()
        return wd.find_element_by_css_selector("strong.search_result, strong.search__found").text

    def get_result_count(self):
        wd = self.app.wd
        self.wait_results()
        text = wd.find_element_by_css_selector("strong.search__found").text
        return int(re.findall("\d+", text)[0])

    def get_all_results_text(self):
        wd = self.app.wd
        self.wait_results()
        return wd.find_element_by_css_selector("ul.info").text
