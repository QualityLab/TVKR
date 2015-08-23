# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait


def test_AP_single_article_view(app):
    wd = app.wd
    app.session.login_as(app.users["admin"])
    app.open_page("admin/article/index")
    wd.find_element_by_xpath("//a[@class='view']").click()
    wait(wd, 60).until(lambda s: len(wd.find_elements_by_xpath("//table[@class='articledispl']")) > 0)
