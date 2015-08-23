# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time

def test_vacancy_create_several_companies(app):
    wd = app.wd
    app.open_page("login")
    app.login(username="z947384@yandex.ru", password="111111")
    time.sleep(5) # даем время залогиниться, без этого фэйлится
    app.open_page("job/vacancy/create")
    time.sleep(5)
    assert wd.find_element_by_xpath("//input[@id='company_398']").is_displayed
    assert wd.find_element_by_xpath("//input[@id='company_399']").is_displayed
    assert wd.find_element_by_xpath("//input[@id='not-exists-company-radio-button']").is_displayed
    assert wd.find_element_by_xpath("//span[.='QA Holdings first']").is_displayed
    assert wd.find_element_by_xpath("//span[.='QA Holdings second']").is_displayed
    