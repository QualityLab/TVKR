# -*- coding: utf-8 -*-
import pytest
from selenium.webdriver.support.wait import WebDriverWait as wait


@pytest.mark.parametrize("link_text,url", [
    ("Обзоры", "article/category2"),
    ("Мнение", "article/category7"),
])
def test_articles_navigation(app, link_text, url):
    wd = app.wd
    app.open_page("article")
    wd.find_element_by_xpath("//ul[@id='yw0']//a[.='%s']" % link_text).click()
    wait(wd, 10).until(lambda s: wd.current_url == app.base_url + url)
