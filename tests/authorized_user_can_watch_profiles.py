# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait


def test_authorized_user_can_watch_profiles(app):
    wd = app.wd
    app.session.login_as(app.users["user1"])
    app.open_page("user/1849")
    wd.find_element_by_link_text("Фотографии").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1[.='Фотографии']"))
    wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Видео']").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1[.='Видео']"))
    wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Мероприятия']").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1[.='Мероприятия']"))
    wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Друзья']").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1[.='Друзья']"))
    wd.find_element_by_xpath("//ul[@id='yw1']//strong[.=' Сообщества']").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//a[.='Подписки']"))
