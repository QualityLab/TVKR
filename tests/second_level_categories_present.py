# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from baseurl import Baseurl

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class second_level_categories_present(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_second_level_categories_present(self):
        success = True
        wd = self.wd
        wd.get(str(Baseurl.baseurl) + "catalog")
        if wd.find_element_by_css_selector("a.catalog__link").text != "Микрофоны":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[1]/ul/li[2]/a").text != "Микшерные пульты":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[1]/ul/li[3]/a").text != "Акустические мониторы":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[1]/ul/li[4]/a").text != "Рекордеры/плееры":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[1]/ul/li[5]/a").text != "Студийное оборудование":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[1]/ul/li[6]/a").text != "Телефонные гибриды":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[1]/ul/li[7]/a").text != "Звуковые карты":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[1]/ul/li[8]/a").text != "Наушники":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[1]/ul/li[9]/a").text != "Гарнитуры":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[1]/ul/li[10]/a").text != "Аппаратура для комментаторов":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[1]/ul/li[11]/a").text != "Оборудование Dolby":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[1]/ul/li[1]/a").text != "Системы автоматизации эфира":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[1]/ul/li[2]/a").text != "Аксессуары":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[1]/ul/li[1]/a").text != "Программное обеспечение":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[1]/ul/li[2]/a").text != "Платы ввода-вывода":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[1]/ul/li[1]/a").text != "Leader":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[1]/ul/li[2]/a").text != "Tektronix":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[1]/ul/li[3]/a").text != "Blackmagic":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[1]/ul/li[4]/a").text != "TSL":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[1]/ul/li[5]/a").text != "Data Video":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[1]/ul/li[6]/a").text != "Прочее":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[1]/ul/li[1]/a").text != "Кабели":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[1]/ul/li[2]/a").text != "Разъемы":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[1]/ul/li[3]/a").text != "Инструменты":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[1]/a").text != "Видеокамеры и камкордеры":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[2]/a").text != "Объективы":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[3]/a").text != "Видеомагнитофоны":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[4]/a").text != "Видеомониторы и системы отображения":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[5]/a").text != "Видеомикшеры, эфирные свитчеры":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[6]/a").text != "Накамерные радиорелейные системы":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[7]/a").text != "Оборудование для организации прямого эфира по сетям сотовой связи":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[8]/a").text != "Процессоры обработки":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[9]/a").text != "Телесуфлеры":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[10]/a").text != "Коммутационно-распределительное оборудование":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[11]/a").text != "Преобразование форматов":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[12]/a").text != "Операторское оборудование":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[1]/div[2]/ul/li[13]/a").text != "Передача видео по IP сетям":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[2]/ul/li[1]/a").text != "Системы автоматизации вещания":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[2]/ul/li[2]/a").text != "Системы хранения данных":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[2]/ul/li[3]/a").text != "Системы автоматизации информационного производства (Newsroom)":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[2]/ul/li[4]/a").text != "Системы графического оформления эфира":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[2]/ul/li[5]/a").text != "Системы для цифрового вещания в форматах IP/ASI и врезки в MPTS":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[2]/ul/li[6]/a").text != "Системы захвата и оцифровки видеоматериала (ingest)":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[2]/ul/li[7]").text != "Системы мониторинга и контрольной записи":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[2]/ul/li[8]/a").text != "Аксессуары":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[2]/div[2]/ul/li[9]/a").text != "Платы ввода-вывода":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[1]/a").text != "Картриджи LTO":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[2]/a").text != "Картриджи для архивов оптических дисков":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[3]/a").text != "Кассеты Betacam SP":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[4]/a").text != "Кассеты Betacam SX":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[5]/a").text != "Кассеты Digital Betacam":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[6]/a").text != "Кассеты DVCAM":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[7]/a").text != "Кассеты HDV":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[8]/a").text != "Кассеты DVCPRO/DVCPRO50":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[9]/a").text != "Кассеты MPEG IMX":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[10]/a").text != "Кассеты HDCAM":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[11]/a").text != "Кассеты HDCAM SR":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[12]/a").text != "Карты P2":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[13]/a").text != "Диски XDCAM":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[14]/a").text != "Карты MS-PX":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[15]/a").text != "Карты SxS":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[16]").text != "Карты XQD":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[17]/a").text != "Карты памяти AXS":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[18]/a").text != "Устройства хранения данных HDD/SSD":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[19]/a").text != "Картриджи GF":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[3]/div[2]/ul/li[20]/a").text != "Карты SRMemory":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[2]/ul/li[1]/a").text != "Цифровые матричные системы":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[2]/ul/li[2]/a").text != "2-х и 4-х проводные системы служебной связи":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[2]/ul/li[3]/a").text != "Беспроводные системы служебной связи":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[2]/ul/li[4]/a").text != "Поясные станции (белтпаки)":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[2]/ul/li[5]/a").text != "Панели абонентов":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[2]/ul/li[6]/a").text != "Интерфейсы":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[4]/div[2]/ul/li[7]/a").text != "Микрофоны, головные гарнитуры и наушники":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[2]/ul/li[1]/a").text != "Направленные светильники":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[2]/ul/li[2]/a").text != "Заполняющие светильники":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[2]/ul/li[3]/a").text != "Комплекты светильников":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[2]/ul/li[4]/a").text != "Приборы управления светом":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[2]/ul/li[5]/a").text != "Блоки питания и кабели":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[2]/ul/li[6]/a").text != "Балласты":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[2]/ul/li[7]/a").text != "Рельсовые системы":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[2]/ul/li[8]/a").text != "Держатели фонов c системой скручивания":
            success = False
            print("verifyText failed")
        if wd.find_element_by_xpath("//div[@class='catalog']/div[5]/div[2]/ul/li[9]/a").text != "Аксессуары":
            success = False
            print("verifyText failed")
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
