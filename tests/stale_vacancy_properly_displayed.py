# -*- coding: utf-8 -*-
import time


def test_stale_vacancy_properly_displayed(app):
    wd = app.wd
    # проверка отображения неавторизованным пользователем
    app.open_page("job/vacancy/view?id=1799")
    time.sleep(5)
    assert "К сожалению, вакансия, которая находилась на этой странице, сейчас неактивна. Но вы можете поискать другие вакансии в сфере кино, теле- и радиовещания, в сервисе «Работа»" in wd.find_element_by_tag_name("body").text
    # проверка отображения авторизованным пользователем
    app.open_page("login")
    app.login(username="123@guerrillamail.com", password="1111")
    time.sleep(3)
    app.open_page("job/vacancy/view?id=1799")
    time.sleep(5)
    assert "К сожалению, вакансия, которая находилась на этой странице, сейчас неактивна. Но вы можете поискать другие вакансии в сфере кино, теле- и радиовещания, в сервисе «Работа»" in wd.find_element_by_tag_name("body").text