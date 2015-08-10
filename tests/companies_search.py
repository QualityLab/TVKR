# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("query,expected", [
    ("3D Media Group", "3D Media Group"),
    ("русские студии", "Всемирные Русские Студии - Санкт-Петербург"),
])

def test_companies_search(app, query, expected):
    wd = app.wd
    wd.get("%s/%s" % (app.base_url, "companies"))
    company_links = wd.find_elements_by_link_text(expected)
    wd.find_element_by_id("keywords").click()
    wd.find_element_by_id("keywords").clear()
    wd.find_element_by_id("keywords").send_keys(query)
    wd.find_element_by_id("filter-by-keywords").click()
    if len(company_links) > 0:
        wait(wd, 30).until(EC.staleness_of(company_links[0]))
    wait(wd, 30).until(lambda s: wd.find_element_by_link_text(expected)).click()
    wait(wd, 30).until(lambda s: wd.find_element_by_css_selector(".company-box"))
