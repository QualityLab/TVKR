# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
import re


class CompanySearchHelper:

    def __init__(self, app):
        self.app = app

    def find(self, query):
        wd = self.app.wd
        self.app.open_companies_page()
        old_companies = wait(wd, 10).until(lambda s: wd.find_elements_by_css_selector("div#companiesList div.items div.line"))
        self.app.type_into(wd.find_element_by_id("keywords"), query)
        wd.find_element_by_id("filter-by-keywords").click()
        if len(old_companies) > 0:
            wait(wd, 10).until(ec.staleness_of(old_companies[0]))

    def wait_results(self):
        wd = self.app.wd
        wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("div#companiesList div.items div.line, div#companiesList div.items div.empty"))

    def get_result_count(self):
        wd = self.app.wd
        self.wait_results()
        text = wd.find_element_by_css_selector("div.search-result").text
        return int(re.findall("\d+", text)[0])

    def get_all_found_titles(self):
        wd = self.app.wd
        self.wait_results()
        return [el.text for el in wd.find_elements_by_css_selector("div#companiesList div.items div.line h2.event__ttl")]
