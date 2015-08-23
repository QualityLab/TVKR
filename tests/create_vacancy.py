# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_create_vacancy_flow(app):
    wd = app.wd
    actions = ActionChains(wd)
    app.session.login_as(app.users["user1"])
    app.open_page("resume")
    title = "Тест создания вакансии %s" % int(time.time())
    wd.find_element_by_xpath("//span[.='Разместить вакансию']").click()
    wait(wd, 60).until(lambda s: wd.find_element_by_xpath("//input[@id='Vacancy_name']"))
    wd.find_element_by_xpath("//input[@id='Vacancy_name']").send_keys(title)
    wd.find_element_by_xpath("//span[@class='select2-chosen' and .='Проф. область']").click()
    wd.find_element_by_xpath("//div[@class='select2-result-label' and .='Кино']").click()
    wd.find_element_by_xpath("//span[@class='select2-chosen' and .='Специальность']").click()
    wd.find_element_by_xpath("//div[@class='select2-result-label' and .='Агент']").click()
    wd.find_element_by_xpath("//span[@class='select2-chosen' and .='Город']").click()
    wd.find_element_by_xpath("//div[@class='select2-result-label' and .='Амстердам']").click()
    wd.find_element_by_xpath("//textarea[@id='Vacancy_smartDescription']").send_keys("Тест создания вакансии")
    wd.find_element_by_xpath("//input[@id='Vacancy_email']").send_keys("vacancy_testing@mail.com")
    wd.find_element_by_xpath("//input[@id='Vacancy_company_name']").send_keys("Sample Company")
    button = wd.find_element_by_xpath("//input[@class='btn btn_green btn_green_big']")
    actions.move_to_element(button).perform()
    wd.find_element_by_xpath("//input[@name='save']").click()
    time.sleep(5) # даем возможность отправиться данным на сервер, без этого ожидания фэйлится
    app.open_page("job") # проверяем, что вакансия НЕ опубликована
    assert title != wd.find_element_by_xpath("//div[@class='items']/div[1]//a").text
    app.open_page("profile") # публикуем
    wd.find_element_by_xpath("//div[@class='user-inf__vacancy line']//a[.='Опубликовать']").click()
    time.sleep(5)
    app.open_page("job") # проверяем, что вакансия успешно опубликована
    assert title == wd.find_element_by_xpath("//div[@class='items']/div[1]//a").text
    app.open_page("profile") # восстанавливаем начальное состояние
    wd.find_element_by_xpath("//div[@class='user-inf__vacancy line']//a[.='Удалить']").click()
    time.sleep(5)
