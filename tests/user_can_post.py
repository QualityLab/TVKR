# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait as wait
import time
from time import gmtime, strftime
import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import gmtime, strftime


def test_user_can_post(app):
    wd = app.wd
    app.open_page("login")
    app.login(username="123@guerrillamail.com", password="1111")
    
    # --------- сообщение с видео -----------
    # если поставить последним в соответствии с номером вкладки - падает с Element Not Visible Exception
    app.open_page("comments/post/index/#tab03") 
    video_text = "Posting video " + strftime("%H:%M:%S", gmtime())
    wd.find_element_by_id("Post_video_link").send_keys("https://youtu.be/WvhmUzvhpx8")
    wd.find_element_by_xpath("//div[@id='tab03']//*[@id='Post_video_name']").send_keys("Sample video name")
    time.sleep(2)
    wd.find_element_by_xpath("//div[@id='tab03']//*[@id='Post_body']").send_keys(video_text)
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//div[@id='tab03']//div[@class='form__bottom']/button")).click()
    time.sleep(3)
    assert video_text in  wd.find_element_by_tag_name("body").text
    
    
    # --------- Текстовое сообщение -----------
    app.open_page("comments/post/index")
    editor = wait(wd, 30).until(lambda s: wd.find_element_by_css_selector("iframe.cke_wysiwyg_frame"))
    wd.switch_to_frame(editor)
    post_text = "Sample post" + strftime("%H:%M:%S", gmtime())
    wait(wd, 30).until(lambda s: wd.find_element_by_css_selector("body")).send_keys(post_text)
    wd.switch_to_default_content()
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//div[@class='form__bottom']/button")).click()
    time.sleep(3)
    assert post_text in  wd.find_element_by_tag_name("body").text  # проверили, что сообщение видно на стене в профиле
    
    # --------- Сообщение с фото -----------
    app.open_page("comments/post/index/#tab02") 
    image_file = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../images/company_logo.jpg"))
    wd.find_element_by_id("Post_image").send_keys(image_file)
    photo_text = "Photo comment" + strftime("%H:%M:%S", gmtime())
    wd.find_element_by_xpath("//div[@id='tab02']//*[@id='Post_body']").send_keys(photo_text)
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//div[@id='tab02']//div[@class='form__bottom']/button")).click()
    time.sleep(3)
    assert photo_text in  wd.find_element_by_tag_name("body").text
    
    # ----------Проверки на странице /community -----------------------
    app.open_page("community")
    assert post_text in  wd.find_element_by_tag_name("body").text
    assert photo_text in  wd.find_element_by_tag_name("body").text
    assert video_text in  wd.find_element_by_tag_name("body").text
    
    # ---------- Зачистка ----------------------------------------------
    app.open_page("comments/post/index")
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//ul[@class='comments messages']/li[1]//a[@class='delete']")).click()
    time.sleep(2)
    alert = wd.switch_to_alert()
    alert.accept()
    time.sleep(5)  # иначе удаляет не то, что нужно
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//ul[@class='comments messages']/li[1]//a[@class='delete']")).click()
    time.sleep(2) # иначе не видит алерт
    alert = wd.switch_to_alert()
    alert.accept()
    time.sleep(5)
    wait(wd, 10).until(lambda s: wd.find_element_by_xpath("//ul[@class='comments messages']/li[1]//a[@class='delete']")).click()
    time.sleep(2)
    alert = wd.switch_to_alert()
    alert.accept()
    time.sleep(5)
    
    
    