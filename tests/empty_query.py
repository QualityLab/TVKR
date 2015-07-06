# -*- coding: utf-8 -*-

def test_empty_query(app):
    app.open_home_page()
    app.search.find("")
    assert app.search.get_result_message() == "Вы задали пустой поисковый запрос"
