# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest


def test_dropdown_first_level_categories_present(app):
    wd = app.wd
    actions = ActionChains(wd)
    app.open_page("")
    menu = wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Оборудование']")
    actions.move_to_element(menu).perform()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Аудио']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Видео']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Радиовещание']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='IT оборудование']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Видеомонтаж']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Профессиональные носители']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Измерительное оборудование']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Системы служебной связи']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Кабели, разъемы']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Осветительное оборудование']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Оборудование DVB-C и DVB-T']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Студийная мебель']").is_displayed()
    assert wd.find_element_by_xpath("//ul[@id='main-menu']//a[.='Аренда']").is_displayed()
        
    
    
