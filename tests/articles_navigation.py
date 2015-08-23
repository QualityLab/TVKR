# -*- coding: utf-8 -*-


def test_articles_navigation(app):
    wd = app.wd
    app.open_home_page()
    wd.find_element_by_link_text("Статьи").click()
    wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Обзоры']").click()
    wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Мнение']").click()
    wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Слова']").click()
    wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Профессия']").click()
    wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Техника']").click()
    wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Практика']").click()
    wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Репортаж']").click()
    wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Инфографика']").click()
    wd.find_element_by_xpath("//ul[@id='yw0']//a[.='Правила профессии']").click()
