# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
from fixture.vacancy import Vacancy


def test_check_vacancy_email(app):
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
    wd.find_element_by_xpath("//input[@class='btn btn_green btn_green_big']").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("div.vacancy"))

    app.session.login_as(app.users["user2"])
    app.open_page("job")
    wd.find_element_by_xpath("//a[.='%s']" % vacancy.title).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("a.create-vacancy-response")).click()
    wait(wd, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.vacancy-response-popup span.btn__inner"))).click()
    wait(wd, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.response-sent")))

    app.session.login_as(app.users["admin"])
    app.open_page("admin/emailQueue")
    assert "vacancy_testing@mail.com" == wd.find_element_by_xpath("//tbody/tr[1]/td[4]").text
