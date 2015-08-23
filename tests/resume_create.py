# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time

def test_resume_create(app):
    wd = app.wd
    app.open_page("login")
    time.sleep(5)
    app.login(username="123@guerrillamail.com", password="1111")
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
    wd.find_element_by_xpath("//input[@name='publish']").click()
    time.sleep(5) # даем возможность отправиться данным на сервер, без этого ожидания фэйлится
    app.open_page("resume") # проверяем публикацию резюме
    assert "Тестовая должность" == wd.find_element_by_xpath("//div[@class='items']/div[1]//a").text
    app.open_page("profile") # восстанавливаем начальное состояние
    wd.find_element_by_xpath("//a[@href='/job/resume/delete' and .='Удалить']").click()
    time.sleep(5)    