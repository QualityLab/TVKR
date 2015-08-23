# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
import time
from fixture.vacancy import Vacancy


def test_create_vacancy_flow(app):
    wd = app.wd
    vacancy = Vacancy(
        title="Тест создания вакансии %s" % int(time.time()),
        area="Кино", role="Агент", location="Амстердам",
        description="Тест создания вакансии",
        email="vacancy_testing@mail.com", company="Sample Company")

    app.session.login_as(app.users["user1"])
    app.vacancy.create_and_save(vacancy)

    assert vacancy.title not in app.vacancy.get_all_published_titles()

    app.open_page("profile") # публикуем
    wd.find_element_by_xpath("//div[@class='user-inf__vacancy line']//a[.='Опубликовать']").click()
    time.sleep(5)

    assert vacancy.title in app.vacancy.get_all_published_titles()

    app.open_page("profile") # восстанавливаем начальное состояние
    wd.find_element_by_xpath("//div[@class='user-inf__vacancy line']//a[.='Удалить']").click()
    time.sleep(5)
