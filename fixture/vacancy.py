# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait


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
