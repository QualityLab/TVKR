# -*- coding: utf-8 -*-
import time
from fixture.vacancy import Vacancy


def test_check_vacancy_email(app):
    wd = app.wd
    vacancy = Vacancy(
        title="Тест создания вакансии %s" % int(time.time()),
        area="Кино", role="Агент", location="Амстердам",
        description="Тест создания вакансии",
        email="vacancy_testing@mail.com", company="Sample Company")

    app.session.login_as(app.users["user1"])
    app.vacancy.create_and_publish(vacancy)

    app.session.login_as(app.users["user2"])
    app.vacancy.open_from_list(vacancy)
    app.vacancy.respond()

    app.session.login_as(app.users["admin"])
    app.open_page("admin/emailQueue")
    assert "vacancy_testing@mail.com" == wd.find_element_by_xpath("//tbody/tr[1]/td[4]").text
