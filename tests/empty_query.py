# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize("input,expected", [
    ("", "Вы задали пустой поисковый запрос"),
    ("a", "Слишком короткий запрос"),
    ("ab", "Слишком короткий запрос"),
    ("abc", "Найдено"),
])
def test_search_query_string_length(app, input, expected):
    app.open_home_page()
    app.search.find(input)
    assert app.search.get_result_message().startswith(expected)
