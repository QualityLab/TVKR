# -*- coding: utf-8 -*-


def test_articles_mnenie_verify(app):
    wd = app.wd
    app.open_page("article/category7")
    for i in range(1,11):
        assert wd.find_element_by_xpath("//div[@class='news news_list']/div[%s]/a[@href='/article/category7']" % i).text == "Мнение"
