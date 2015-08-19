# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_check_vacancy_email(app):
    wd = app.wd
    actions = ActionChains(wd)
    app.open_page("resume") # размещаем вакансию с известным нам e-mail для ответа
    wd.find_element_by_xpath("//span[.='Разместить вакансию']").click()
    app.login(username="123@guerrillamail.com", password="1111")
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//input[@id='Vacancy_name']"))
    wd.find_element_by_xpath("//input[@id='Vacancy_name']").send_keys("Тест создания вакансии")
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
    wd.find_element_by_xpath("//input[@class='btn btn_green btn_green_big']").click()
    time.sleep(3) # даем возможность отправиться данным на сервер, без этого ожидания фэйлится
    app.open_page("logout")
    app.open_page("login") # откликаемся на вакансию пользователем, у которого уже есть тестовое резюме 
    app.login(username="z947384@yandex.ru", password="111111")
    app.open_page("job")
    wd.find_element_by_xpath("//a[.='Тест создания вакансии']").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//span[@class='btn__inner']"))
    wd.find_element_by_xpath("//span[@class='btn__inner']").click()
    wd.find_element_by_xpath("//span[.='Отправить отклик']").click() #пробовал обратиться через разные атрибуты, в xpath элемент виден без проблем
    time.sleep(5)
    app.open_page("logout")
    app.open_page("login") # проверяем на какой e-mail ушел отклик
    app.login(username="testtvkinoradio@gmail.com", password="test12")
    time.sleep(5) # даем время залогиниться
    app.open_page("admin/emailQueue")
    assert "vacancy_testing@mail.com" == wd.find_element_by_xpath("//tbody/tr[1]/td[4]").text