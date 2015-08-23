# -*- coding: utf-8 -*-
import time

def test_add_friend_flow(app):
    wd = app.wd
    app.session.login_as(app.users["user1"])
    app.open_page("user/user/view?id=2596")
    wd.find_element_by_xpath("//div[@class='profile__meta-status']//span[.='Добавить в друзья']").click()
    assert len(wd.find_elements_by_xpath("//a[.='Олеся Подробная']")) > 0
    assert "Заявка отправлена" in wd.find_element_by_tag_name("html").text
    assert len(wd.find_elements_by_xpath("//a[.='Отменить']")) > 0
    app.open_page("user/friends/list/#tab03")
    assert len(wd.find_elements_by_xpath("//a[@href=\"/user/2596\"]")) > 0

    #возвращаем систему в исходное состояние - отменяем заявку
    app.open_page("user/friends/list#tab03")
    wd.find_element_by_xpath("//a[.='Отменить']").click()
    time.sleep(2)
