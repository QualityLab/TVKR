# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait


def test_company_create(app):
    wd = app.wd
    app.open_page("login")
    app.login(username="123@guerrillamail.com", password="1111")
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//span[.='Добавить компанию']"))
    wd.find_element_by_xpath("//span[.='Добавить компанию']").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//input[@id='Company_title']"))
    wd.find_element_by_xpath("//input[@id='Company_title']").send_keys("Sample company")
    wd.find_element_by_xpath("//li//span[.='Оборудование']").click()
    #попытка переключиться во фрейм wysiwyg и ввести текст
    editor = wd.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']")
    wd.switch_to_frame().frame(editor)
    wd.find_element_by_tag("body").send_keys("Sample description")
    
    