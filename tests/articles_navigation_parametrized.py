# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import pytest


@pytest.mark.parametrize("locator,url", [
        ("//ul[@id='yw0']//a[.='Обзоры']", "article/category2"),
        ("//ul[@id='yw0']//a[.='Мнение']", "article/category7")
    ])
def test_articles_navigation(app, locator, url):
    wd = app.wd
    app.open_page("article")
    wd.find_element_by_xpath(str(locator)).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1"))
    assert wd.current_url == app.base_url + url
