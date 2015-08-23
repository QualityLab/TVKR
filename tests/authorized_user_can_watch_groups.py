# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait


def test_authorized_user_can_watch_groups(app):
    wd = app.wd
    app.session.login_as(app.users["user1"])
    app.open_page("group/253/members")
    wd.find_element_by_link_text("Фотографии").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1[.='Фотографии']"))
    wd.find_element_by_link_text("Участники").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1[.='Участники']"))
    wd.find_element_by_link_text("Видео").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1[.='Видео']"))
    wd.find_element_by_link_text("Лента").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//a[.='Сообщение']"))
