# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

def test_empty_query(app):
    success = True
    wd = app.wd
    wd.get("http://tvkinoradio.ru/")
    wd.find_element_by_id("header-search").click()
    wd.find_element_by_id("header-search").clear()
    wd.find_element_by_id("header-search").send_keys()
    wd.find_element_by_css_selector("input.btn_search").click()
    if wd.find_element_by_css_selector("strong.search_result").text != "Вы задали пустой поисковый запрос":
        success = False
        print("verifyText failed")
    assert(success)
