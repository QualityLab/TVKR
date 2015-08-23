# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time, pytest
from baseurl import Baseurl
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.parametrize("locator,url", [
        ("//ul[@id='main-menu']//a[.='Обзоры']", "article/2/list"),
        ("//ul[@id='main-menu']//a[.='Профессия']", "article/9/list"),
        ("//ul[@id='main-menu']//a[.='Слова']", "article/8/list"),
        ("//ul[@id='main-menu']//a[.='Мнение']", "article/7/list"),
        ("//ul[@id='main-menu']//a[.='Техника']", "article/10/list"),
        ("//ul[@id='main-menu']//a[.='Практика']", "article/11/list"),
        ("//ul[@id='main-menu']//a[.='Репортаж']", "article/12/list"),
        ("//ul[@id='main-menu']//a[.='Инфографика']", "article/13/list"),
        ("//ul[@id='main-menu']//a[.='Правила профессии']", "article/16/list"),
        #("//ul[@id='main-menu']//a[.='Тест']", "article/17/list"),
    ])
def test_articles_dropdown_navigation(app, locator, url):
    wd = app.wd
    actions = ActionChains(wd)
    app.open_page("") # home page
    time.sleep(2)
    menu = wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Статьи']")
    actions.move_to_element(menu).perform()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath(str(locator)))
    wd.find_element_by_xpath(str(locator)).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1"))
    assert wd.current_url == str(Baseurl.baseurl) + url	