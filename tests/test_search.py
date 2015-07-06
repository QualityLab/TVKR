# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize("query,expected", [
    ("", "Вы задали пустой поисковый запрос"),
    ("a", "Слишком короткий запрос"),
    ("ab", "Слишком короткий запрос"),
    ("sony", "Найдено"),
])
def test_search_by_query_string_of_various_length(app, query, expected):
    app.open_home_page()
    app.search.find(query)
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
    assert app.search.get_result_count() > 0
    assert expected in app.search.get_all_results_text()
