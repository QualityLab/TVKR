# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class users_profile_is_properly_displayed(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_users_profile_is_properly_displayed(self):
        success = True
        wd = self.wd
        wd.get("http://tvkinoradio.ru")
        wd.find_element_by_link_text("Войти").click()
        wd.find_element_by_id("UserForm_email").click()
        wd.find_element_by_id("UserForm_email").clear()
        wd.find_element_by_id("UserForm_email").send_keys("123@guerrillamail.com")
        wd.find_element_by_id("UserForm_password").click()
        wd.find_element_by_id("UserForm_password").clear()
        wd.find_element_by_id("UserForm_password").send_keys("1111")
        wd.find_element_by_id("submit_link").click()
        if not (len(wd.find_elements_by_css_selector("div.company-box__photo > img")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_css_selector("h2.company-box__ttl")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@class='company-box__entry']/a")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//ul[@id='yw0']//a[.=' Сообщения']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//ul[@id='yw0']//a[.=' Компании']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//ul[@id='yw0']//a[.=' Резюме']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//ul[@id='yw0']//a[.=' Вакансии']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//ul[@id='yw1']//strong[.=' Лента']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//ul[@id='yw1']//strong[.=' Фотографии']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//ul[@id='yw1']//strong[.=' Видео']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//ul[@id='yw1']//strong[.=' Мероприятия']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//ul[@id='yw1']//strong[.=' Друзья']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//ul[@id='yw1']//strong[.=' Сообщества']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@class='user-inf']//h2[.='Мои компании']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_link_text("Добавить компанию")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@class='user-inf']//h2[.='Резюме']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_link_text("Создать резюме")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_xpath("//div[@class='user-inf']//h2[.='Вакансии']")) != 0):
            success = False
            print("verifyElementPresent failed")
        if not (len(wd.find_elements_by_link_text("Добавить вакансию")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
