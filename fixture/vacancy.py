# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ec


class Vacancy:

    def __init__(self, title, area, role, location, description, email, company):
        self.title = title
        self.area = area
        self.role = role
        self.location = location
        self.description = description
        self.email = email
        self.company = company


class VacancyHelper:

    def __init__(self, app):
        self.app = app

    def create_and_publish(self, vacancy):
        self.init_vacancy_creation()
        self.fill_vacancy_form(vacancy)
        self.publish()

    def create_and_save(self, vacancy):
        self.init_vacancy_creation()
        self.fill_vacancy_form(vacancy)
        self.save()

    def init_vacancy_creation(self):
        wd = self.app.wd
        self.app.open_page("resume")
        wd.find_element_by_xpath("//span[.='Разместить вакансию']").click()
        wait(wd, 60).until(lambda s: wd.find_element_by_xpath("//input[@id='Vacancy_name']"))

    def fill_vacancy_form(self, vacancy):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@id='Vacancy_name']").send_keys(vacancy.title)
        wd.find_element_by_xpath("//span[@class='select2-chosen' and .='Проф. область']").click()
        wd.find_element_by_xpath("//div[@class='select2-result-label' and .='%s']" % vacancy.area).click()
        wd.find_element_by_xpath("//span[@class='select2-chosen' and .='Специальность']").click()
        wd.find_element_by_xpath("//div[@class='select2-result-label' and .='%s']" % vacancy.role).click()
        wd.find_element_by_xpath("//span[@class='select2-chosen' and .='Город']").click()
        wd.find_element_by_xpath("//div[@class='select2-result-label' and .='%s']" % vacancy.location).click()
        wd.find_element_by_xpath("//textarea[@id='Vacancy_smartDescription']").send_keys(vacancy.description)
        wd.find_element_by_xpath("//input[@id='Vacancy_email']").send_keys(vacancy.email)
        wd.find_element_by_xpath("//input[@id='Vacancy_company_name']").send_keys(vacancy.company)

    def publish(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='publish']").click()
        wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("div.vacancy"))

    def save(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='save']").click()
        wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("div.vacancy"))

    def open_from_list(self, vacancy):
        wd = self.app.wd
        self.app.open_page("job")
        wd.find_element_by_xpath("//a[.='%s']" % vacancy.title).click()
        wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("div.vacancy"))

    def respond_to(self, vacancy):
        wd = self.app.wd
        self.open_from_list(vacancy)
        wait(wd, 10).until(lambda s: wd.find_element_by_css_selector("a.create-vacancy-response")).click()
        wait(wd, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.vacancy-response-popup span.btn__inner"))).click()
        wait(wd, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.response-sent")))

    def get_all_published_titles(self):
        wd = self.app.wd
        self.app.open_page("job")
        return [el.text for el in wd.find_elements_by_css_selector("div.items a")]
