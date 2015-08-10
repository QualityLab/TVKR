# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

def test_companies_search_partly_match(app):
    wd = app.wd
    wd.get("%s/%s" % (app.base_url, "companies"))
    company_links = wd.find_elements_by_link_text("3D Media Group")
    wd.find_element_by_id("keywords").click()
    wd.find_element_by_id("keywords").clear()
    wd.find_element_by_id("keywords").send_keys("русские студии")
    wd.find_element_by_id("filter-by-keywords").click()
    if len(company_links) > 0:
        wait(wd, 30).until(EC.staleness_of(company_links[0]))
    wait(wd, 30).until(lambda s: wd.find_element_by_link_text("Всемирные Русские Студии - Санкт-Петербург")).click()
    # тут надо добавить ожидание загрузки страницы компании
