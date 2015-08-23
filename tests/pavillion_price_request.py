# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time, datetime
from time import gmtime, strftime

def test_pavillion_price_request(app):
    wd = app.wd
    app.open_page("pavilions/97")
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//span[.='Запросить стоимость']")).click()
    app.login(username="z947384@yandex.ru", password="111111")
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//span[.='Запросить стоимость']")).click()
    # пока не удалось, но нужно устанавливать будущие даты
    # first_date = datetime.date.today() + datetime.timedelta(days=2) # дата начала срока аренды
    # last_date = datetime.date.today() + datetime.timedelta(days=5)  # дата конца срока аренды
    current_date = strftime("%d.%m.%Y", gmtime())
    wait(wd, 10).until(lambda s: wd.find_element_by_id("PavilionRequest_date_from")).send_keys(current_date)
    wait(wd, 10).until(lambda s: wd.find_element_by_id("PavilionRequest_date_to")).send_keys(current_date)
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]")).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]")).click()
    # добавить проверку текста уведомления в админке
    
    
    
     