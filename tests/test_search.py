# -*- coding: utf-8 -*-
import pytest
import time


@pytest.mark.parametrize("query", [
    ("Neumann"),
    ("кинокамера"),
    ("компания Sony"),
])
def test_search_positiff(app, query):
    app.open_home_page()
    app.search.find(query)
    time.sleep(3)
    assert app.search.get_result_count() > 0
    assert query in app.search.get_all_results_text()


@pytest.mark.parametrize("query,expected", [
    ("", "Вы задали пустой поисковый запрос"),
    ("a", "Слишком короткий запрос"),
    ("ab", "Слишком короткий запрос"),
    ("sony", "Найдено"),
])
def test_search_by_query_string_of_various_length(app, query, expected):
    app.open_home_page()
    app.search.find(query)
    time.sleep(3)
    assert app.search.get_result_message().startswith(expected)


@pytest.mark.parametrize("query,expected", [
    ("千代に 細石", "Некорректный запрос. Попробуйте изменить запрос"),
    ("камера 千代に Arri", "Поиск осуществлен по ключевым словам « камера Arri », по « 千代に » поиск не возможен."),
])
def test_search_in_wrong_encoding(app, query, expected):
    app.open_home_page()
    app.search.find(query)
    time.sleep(3)
    assert app.search.get_result_message().startswith(expected)


@pytest.mark.parametrize("query,expected", [
    ("кино*показ", "кинопоказ"),
    ("*anasonic", "panasonic"),
    ("sonif*", "sonifex"),
    ("кинофе*валь", "кинофестиваль"),
    ("?частник", "участник"),
    ("Sennheise?", "Sennheiser"),
    ("ре?иссер", "режиссер"),
])
def test_search_by_patterns(app, query, expected):
    app.open_home_page()
    app.search.find(query)
    time.sleep(3)
    assert app.search.get_result_count() > 0
    assert expected in app.search.get_all_results_text()

@pytest.mark.parametrize("query1,query2", [
    ("оборудование", "ОБОРУДОВАНИЕ"),
    ("оборудование", "Оборудование"),
    ("оборудование", "обоРудование"),
    ("оборудование", "ОбОРУдОвАнИЕ"),
    ("видео монтаж", "монтаж видео"),
    ("фестиваль", "фёстиваль"),
])
def test_search_is_case_insensitive_and_order_independent_and_yo(app, query1, query2):
    app.open_home_page()
    app.search.find(query1)
    time.sleep(2)
    res1 = app.search.get_result_count()
    app.search.find(query2)
    time.sleep(2)
    res2 = app.search.get_result_count()
    assert res1 > 0
    assert res1 == res2