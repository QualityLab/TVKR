from selenium import webdriver
from fixture.session import User
from .session import SessionHelper
from .search import SearchHelper
from .companies_search import CompanySearchHelper
from .vacancy import VacancyHelper
from selenium.webdriver.support.wait import WebDriverWait as wait


class Application:

    def __init__(self, browser, remote, config):
        if remote:
            self.wd = webdriver.Remote(command_executor=remote, desired_capabilities={"browserName": browser})
        else:
            if browser == "firefox":
                self.wd = webdriver.Firefox()
            elif browser == "chrome":
                self.wd = webdriver.Chrome()
            elif browser == "ie":
                self.wd = webdriver.Ie()
            else:
                raise ValueError("Unrecognized browser %s" % browser)
        self.config = config
        self.base_url = config['web']['baseUrl']

        self.users = {}
        for key in config['users']:
            self.users[key] = User(
                username=config['users'][key]['username'],
                password=config['users'][key]['password'],
                real_name=config['users'][key]['real_name'],
                role=config['users'][key]['role'])

        self.session = SessionHelper(self)
        self.search = SearchHelper(self)
        self.vacancy = VacancyHelper(self)
        self.companies_search = CompanySearchHelper(self)

        self.open_home_page()
        
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_page(self, url): # открывает произвольную страницу, часть адреса которой, идущая после base_url, передается как аргумент
        wd = self.wd
        wd.get(self.base_url + url)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
        
    def open_companies_page(self):
        wd = self.wd
        wd.get("%s/%s" % (self.base_url, "companies"))

    def type_into(self, web_element, text):
        web_element.click()
        web_element.clear()
        web_element.send_keys(text)

    def destroy(self):
        self.wd.quit()
        
    def login(self, username, password): # метод заполняет поля и кликает сабмит на УЖЕ открытой странице авторизации
        wd = self.wd
        wait(wd, 10).until(lambda s: wd.find_element_by_id('UserForm_email'))
        wd.find_element_by_id('UserForm_email').send_keys(username)
        wd.find_element_by_id('UserForm_password').send_keys(password)
        wd.find_element_by_id('submit_link').click()
