# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time


def test_community_search_filters_apply(app):
    wd = app.wd
    app.open_page("community?search_text=конкурсы&category=&specialty=&town=") # запрос без фильтров
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//a[@href='/group/253/status']"))
    app.open_page("community?search_text=конкурсы&category=9&specialty=&town=") # запрос с фильтром "проф.область"
    time.sleep(3)
    assert "К сожалению, по вашему запросу ничего не найдено. Попробуйте изменить запрос или сбросить фильтры поиска." in wd.find_element_by_tag_name("body").text
    app.open_page("community?search_text=конкурсы&category=&specialty=95&town=") # запрос с фильтром "специальность"
    time.sleep(3)
    assert "К сожалению, по вашему запросу ничего не найдено. Попробуйте изменить запрос или сбросить фильтры поиска." in wd.find_element_by_tag_name("body").text
    app.open_page("community?search_text=конкурсы&category=&specialty=&town=1") # запрос с фильтром "город"
    time.sleep(3)
    assert "К сожалению, по вашему запросу ничего не найдено. Попробуйте изменить запрос или сбросить фильтры поиска." in wd.find_element_by_tag_name("body").text