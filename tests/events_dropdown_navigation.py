# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time, pytest
from baseurl import Baseurl
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.parametrize("locator,url", [
        ("//ul[@id='main-menu']//a[.='Кинопоказ']", "events/category/1"),
        ("//ul[@id='main-menu']//a[.='Фестиваль']", "events/category/2"),
        ("//ul[@id='main-menu']//a[.='Выставка']", "events/category/4"),
        ("//ul[@id='main-menu']//a[.='Мастер-класс']", "events/category/5"),
        ("//ul[@id='main-menu']//a[.='Презентация']", "events/category/6"),
        ("//ul[@id='main-menu']//a[.='Форум']", "events/category/7"),
        ("//ul[@id='main-menu']//a[.='Конкурс']", "events/category/8"),
        ("//ul[@id='main-menu']//a[.='Лекция']", "events/category/9"),
        ("//ul[@id='main-menu']//a[.='Курсы']", "events/category/10"),
        ("//ul[@id='main-menu']//a[.='Кастинг']", "events/category/11"),
        ("//ul[@id='main-menu']//a[.='Семинары']", "events/category/12"),
    ])
def test_events_dropdown_navigation(app, locator, url):
    wd = app.wd
    actions = ActionChains(wd)
    wd.get(str(Baseurl.baseurl))
    menu = wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='События']")
    actions.move_to_element(menu).perform()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath(str(locator)))
    wd.find_element_by_xpath(str(locator)).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1"))
    assert wd.current_url == str(Baseurl.baseurl) + url	