# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import os.path
import time

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
    editor = wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("iframe.cke_wysiwyg_frame"))
    wd.switch_to_frame(editor)
    wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("body")).send_keys("Sample description")
    wd.switch_to_default_content()
    image_file = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images/company_logo.jpg"))
    wd.find_element_by_name("image").send_keys(image_file)
    wait(wd, 10).until(lambda s: wd.find_element_by_id("button_crop_recortar")).click()
    crop_button = wait(wd, 10).until(ec.element_to_be_clickable((By.ID, "button_crop_original")))
    time.sleep(2)
    crop_button.click()
    wait(wd, 10).until(ec.staleness_of(crop_button))
    pass