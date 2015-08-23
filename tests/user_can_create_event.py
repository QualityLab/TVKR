# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import os.path
import time
from time import gmtime, strftime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


def test_user_can_create_event(app):
    wd = app.wd
    app.session.login_as(app.users["user2"])
    app.open_page("events")
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//span[.='Создать событие']")).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//span[@class='select2-chosen']")).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//div[@class='select2-result-label' and .='Кастинг']")).click()
    event_name = "Тест создания" + strftime("%H:%M:%S", gmtime()) # делаем имя уникальным для возможности повторного запуска
    wd.find_element_by_id("Event_title").send_keys(event_name)
    image_file = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images/event_logo.jpg"))
    wd.find_element_by_name("image").send_keys(image_file)
    wait(wd, 60).until(lambda s: wd.find_element_by_id("button_crop_recortar")).click()
    crop_button = wait(wd, 60).until(ec.element_to_be_clickable((By.ID, "button_crop_original")))
    time.sleep(5)
    crop_button.click()
    wait(wd, 60).until(ec.staleness_of(crop_button))
    current_date = strftime("%m/%d/%Y", gmtime()) #переделать на генерацию будущих дат
    wait(wd, 10).until(lambda s: wd.find_element_by_id("Event_start_date")).send_keys(current_date)
    wait(wd, 10).until(lambda s: wd.find_element_by_id("Event_end_date")).send_keys(current_date)
    wait(wd, 10).until(lambda s: wd.find_element_by_id("town_id")).send_keys("Москва")
    wait(wd, 10).until(lambda s: wd.find_element_by_id("Event_address")).send_keys("Адрес события, 123")
    editor = wait(wd, 60).until(lambda s: wd.find_element_by_css_selector("iframe.cke_wysiwyg_frame"))
    wd.switch_to_frame(editor)
    wait(wd, 60).until(lambda s: wd.find_element_by_css_selector("body")).send_keys("Sample description")
    wd.switch_to_default_content()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//input[@class='btn btn_green']")).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1"))
    assert wd.find_element_by_xpath("//h1").text == event_name
    #можно добавить удаление в админке
    