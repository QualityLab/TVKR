# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time

def test_resume_save_then_publish(app):
    wd = app.wd
    app.session.login_as(app.users["user1"])
    wait(wd, 60).until(lambda s: wd.find_element_by_xpath("//span[.='Создать резюме']"))
    wd.find_element_by_xpath("//span[.='Создать резюме']").click()
    wait(wd, 60).until(lambda s: wd.find_element_by_xpath("//input[@id='Resume_post']")) # вводим данные в форму резюме
    wd.find_element_by_xpath("//span[.='Параметры']").click()
    wd.find_element_by_xpath("//input[@id='Resume_post']").send_keys("Тестовая должность")
    wd.find_element_by_xpath("//label[.='Администрация']").click()
    wd.find_element_by_xpath("//div[@id='s2id_autogen1']//span[@class='select2-chosen']").click()
    wd.find_element_by_xpath("//div[@class='select2-result-label' and .='Администратор']").click()
    wd.find_element_by_xpath("//div[@id='s2id_autogen3']//span[@class='select2-chosen']").click()
    wd.find_element_by_xpath("//div[@class='select2-result-label' and .='Свободный график']").click()
    wd.find_element_by_xpath("//dl[@class='accordion']//dt[4]").click()
    wd.find_element_by_xpath("//div[@id='s2id_autogen7']//span[@class='select2-chosen']").click()
    wd.find_element_by_xpath("//div[@class='select2-result-label' and .='Высшее']").click()
    wd.find_element_by_xpath("//input[@name='save']").click()
    time.sleep(5) # даем возможность отправиться данным на сервер, без этого ожидания фэйлится
    app.open_page("resume") # проверяем, что вакансия НЕ опубликована
    assert "Тест создания вакансии" != wd.find_element_by_xpath("//div[@class='items']/div[1]//a").text
    app.open_page("profile") # публикуем
    wd.find_element_by_xpath("//div[@class='user-inf__resume line']//a[.='Опубликовать']").click()
    time.sleep(5)
    app.open_page("resume") # проверяем, что вакансия успешно опубликована
    assert "Тестовая должность" == wd.find_element_by_xpath("//div[@class='items']/div[1]//a").text
    app.open_page("profile") # восстанавливаем начальное состояние
    wd.find_element_by_xpath("//div[@class='user-inf__resume line']//a[.='Удалить']").click()
    time.sleep(5)