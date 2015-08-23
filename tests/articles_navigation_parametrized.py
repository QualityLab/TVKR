# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time, pytest
from baseurl import Baseurl


@pytest.mark.parametrize("locator,url", [
        ("//ul[@id='yw0']//a[.='Обзоры']", "article/category2"),
        ("//ul[@id='yw0']//a[.='Мнение']", "article/category7")
    ])
def test_articles_navigation(app, locator, url):
    wd = app.wd
    wd.get(str(Baseurl.baseurl) + "/article")
    wd.find_element_by_xpath(str(locator)).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1"))
    assert wd.current_url == str(Baseurl.baseurl) + url
    