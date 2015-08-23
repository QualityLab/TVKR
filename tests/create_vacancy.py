# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
import time
from fixture.vacancy import Vacancy


def test_create_vacancy_flow(app):
    wd = app.wd
    actions = ActionChains(wd)
    vacancy = Vacancy(
        title="Тест создания вакансии %s" % int(time.time()),
        area="Кино", role="Агент", location="Амстердам",
        description="Тест создания вакансии",
        email="vacancy_testing@mail.com", company="Sample Company")

    app.session.login_as(app.users["user1"])
    app.vacancy.init_vacancy_creation()
    app.vacancy.fill_vacancy_form(vacancy)

    button = wd.find_element_by_xpath("//input[@class='btn btn_green btn_green_big']")
    actions.move_to_element(button).perform()
    wd.find_element_by_xpath("//input[@name='save']").click()
    time.sleep(5) # даем возможность отправиться данным на сервер, без этого ожидания фэйлится

    app.open_page("job") # проверяем, что вакансия НЕ опубликована
    assert vacancy.title != wd.find_element_by_xpath("//div[@class='items']/div[1]//a").text

    app.open_page("profile") # публикуем
    wd.find_element_by_xpath("//div[@class='user-inf__vacancy line']//a[.='Опубликовать']").click()
    time.sleep(5)

    app.open_page("job") # проверяем, что вакансия успешно опубликована
    assert vacancy.title == wd.find_element_by_xpath("//div[@class='items']/div[1]//a").text

    app.open_page("profile") # восстанавливаем начальное состояние
    wd.find_element_by_xpath("//div[@class='user-inf__vacancy line']//a[.='Удалить']").click()
    time.sleep(5)
