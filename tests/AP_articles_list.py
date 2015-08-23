# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from baseurl import Baseurl


    
def test_AP_articles_list(app):
    wd = app.wd
    app.open_page("login")
    app.login(username="testtvkinoradio@gmail.com", password="test12")
    app.open_page("admin/article/index")
    assert len(wd.find_elements_by_xpath("//h1[.='Статьи']")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c0']//a[.='#']")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c1']//a[.='Название']")) != 0
    assert len(wd.find_elements_by_xpath("//div[@id='article-grid']//th[.='Изображение']")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c3']//a[.='Категория']")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c4']//a[.='Опубликована']")) != 0
    assert len(wd.find_elements_by_xpath("//div[@id='article-grid']//th[.='Автор']")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c6']//a[.='Состояние']")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c7']//a[.='Просмотры']")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c8']//a[.='Читатели']")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c9']/a[@href=\"/admin/article/index?Article_sort=countVkLike\"]")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c10']/a[@href=\"/admin/article/index?Article_sort=countFbLike\"]")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c11']/a[@href=\"/admin/article/index?Article_sort=countTwLike\"]")) != 0
    assert len(wd.find_elements_by_xpath("//th[@id='article-grid_c12']/a[@href=\"/admin/article/index?Article_sort=countGpLike\"]")) != 0
    assert len(wd.find_elements_by_css_selector("#Article_id")) != 0
    assert len(wd.find_elements_by_css_selector("#Article_name")) != 0
    assert len(wd.find_elements_by_css_selector("#Article_category_id")) != 0
    assert len(wd.find_elements_by_id("Article_published_at")) != 0
    assert len(wd.find_elements_by_id("Article_status")) != 0
    assert len(wd.find_elements_by_xpath("//tr[@class='odd']")) != 0
    assert len(wd.find_elements_by_xpath("//tr[@class='even']")) != 0
            