# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize("query,expected", [
    ("3D Media Group", "3D Media Group"),
    ("русские студии", "Всемирные Русские Студии - Санкт-Петербург"),
])
def test_companies_search(app, query, expected):
    app.companies_search.find(query)
    assert app.companies_search.get_result_count() > 0
    assert expected in app.companies_search.get_all_found_titles()
