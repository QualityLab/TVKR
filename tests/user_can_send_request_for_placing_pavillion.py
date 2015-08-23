# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time

def test_user_can_send_request_for_placing_pavillion(app):
    wd = app.wd
    app.session.login_as(app.users["user2"])
    app.open_page("pavilions?town=1")
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//span[.='Разместить павильон']")).click()
    time.sleep(5)
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h1[.='Размещение павильонов']"))
    assert "Если вы предоставляете в аренду павильоны для кино-, теле-, видео-, или фотосъемки, вы можете опубликовать на нашем сайте информацию о ваших услугах." in wd.find_element_by_tag_name("body").text
    wait(wd, 10).until(lambda s: wd.find_element_by_id("open-popup")).click()
    wait(wd, 10).until(lambda s: wd.find_element_by_id("PavilionRequest_phone")).send_keys("+7(495) 123-456")
    wd.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button[1]").click()
    wait(wd, 10).until(lambda s: wd.find_element_by_id("request-success"))
    wd.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button").click()
    # потом добавить проверку текста письма в админке