# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time


def test_pavillions_list_displayed_properly(app):
    wd = app.wd
    app.open_page("pavilions?town=1")
    assert wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//a[@data-value='1']")).is_displayed()  # теги с назначением павильона
    assert wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//a[@data-value='2']")).is_displayed()
    assert wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//a[@data-value='3']")).is_displayed()
    assert wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//a[@data-value='4']")).is_displayed()
    assert wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//a[@class='map-pin']/sup")).is_displayed()  # геотег
    assert wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//a[@class='pavilion-image fancybox']/img")).is_displayed()  # фото
    assert wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//h2[@class='pavilion-name']/a")).is_displayed()  # название павильона
    assert wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//div[@class='pavilion-info line']/ul/li/strong")).is_displayed()  # название компании, нет атрибутов чтобы обратиться иначе
    assert wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//div[@class='pavilion-info line']/ul/li/i[@class='ico ico_place']")).is_displayed()  # указание города
    assert wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//div[@class='pavilion-info line']/ul/li[@class='price']/a")).is_displayed()  # ссылка на запрос стоимости