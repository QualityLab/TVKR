# -*- coding: utf-8 -*-


def test_accessories_present(app):
    wd = app.wd
    app.open_page("catalog/video_13/videokameri-i-kamkorderi_128/xdcam_460/product_12700_pxw-x200")
    wd.find_element_by_xpath("//ul[@class='tabset']//a[.='Аксессуары']").click()
    wd.find_element_by_link_text("Аккумуляторы для видеокамер DV, HDV, XDCAM EX и др.").click()
    assert len(wd.find_elements_by_css_selector("div.category__block.line")) != 0
            
            