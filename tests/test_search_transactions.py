from collections import Counter
from typing import Dict, List

import pytest

from src.search_transactions import process_bank_operations, process_bank_search


@pytest.fixture
def sample_data():
    return [
        {"amount": 1000, "description": "Оплата в супермаркете Магнит"},
        {"amount": 500, "description": "Перевод на карту другу"},
        {"amount": 200, "description": "Оплата в супермаркете Пятерочка"},
        {"amount": 300, "description": "Оплата коммунальных услуг ЖКХ"},
        {"amount": 400, "description": "Перевод средств родственнику"},
        {"amount": 600, "description": "Покупка в магазине"},
    ]


def test_basic_search(sample_data):
    result = process_bank_search(sample_data, "супермаркете")
    expected = [
        {"amount": 1000, "description": "Оплата в супермаркете Магнит"},
        {"amount": 200, "description": "Оплата в супермаркете Пятерочка"},
    ]
    assert result == expected


def test_case_insensitive_search(sample_data):
    result = process_bank_search(sample_data, "ПЕРЕВОД")
    expected = [
        {"amount": 500, "description": "Перевод на карту другу"},
        {"amount": 400, "description": "Перевод средств родственнику"},
    ]
    assert result == expected


def test_partial_match_search(sample_data):
    result = process_bank_search(sample_data, "оплата")
    expected = [
        {"amount": 1000, "description": "Оплата в супермаркете Магнит"},
        {"amount": 200, "description": "Оплата в супермаркете Пятерочка"},
        {"amount": 300, "description": "Оплата коммунальных услуг ЖКХ"},
    ]
    assert result == expected


# Тест с точным совпадением слова
def test_exact_word_search(sample_data):
    result = process_bank_search(sample_data, "магазине")
    expected = [{"amount": 600, "description": "Покупка в магазине"}]
    assert result == expected


# Тест с отсутствующими результатами
def test_no_results_search(sample_data):
    result = process_bank_search(sample_data, "кафе")
    assert result == []


# Тест с пустыми данными
def test_empty_data_search():
    result = process_bank_search([], "любой_поиск")
    assert result == []


# Тест с None в описании
def test_none_description_search(sample_data):
    # Добавляем операцию с None в description
    modified_data = sample_data + [{"amount": 100, "description": None}]
    result = process_bank_search(modified_data, "перевод")
    expected = [
        {"amount": 500, "description": "Перевод на карту другу"},
        {"amount": 400, "description": "Перевод средств родственнику"},
    ]
    assert result == expected


def test_special_characters_search(sample_data):
    result = process_bank_search(sample_data, "Магнит")
    expected = [{"amount": 1000, "description": "Оплата в супермаркете Магнит"}]
    assert result == expected


def test_whitespace_search(sample_data):
    result = process_bank_search(sample_data, " в ")
    expected = [
        {"amount": 1000, "description": "Оплата в супермаркете Магнит"},
        {"amount": 200, "description": "Оплата в супермаркете Пятерочка"},
        {"amount": 600, "description": "Покупка в магазине"},
    ]
    assert result == expected


@pytest.fixture
def sample_data():
    return [
        {"amount": 1000, "description": "Оплата в супермаркете Магнит"},
        {"amount": 500, "description": "Перевод на карту другу"},
        {"amount": 200, "description": "Оплата в супермаркете Пятерочка"},
        {"amount": 300, "description": "Оплата коммунальных услуг ЖКХ"},
        {"amount": 400, "description": "Перевод средств родственнику"},
        {"amount": 600, "description": "Покупка в магазине"},
    ]


@pytest.fixture
def sample_categories():
    return ["супермаркет", "перевод", "жкх", "магазин"]


def test_basic_functionality(sample_data, sample_categories):
    result = process_bank_operations(sample_data, sample_categories)
    expected = {"супермаркет": 2, "перевод": 2, "жкх": 1, "магазин": 1}
    assert result == expected


def test_empty_data(sample_categories):
    result = process_bank_operations([], sample_categories)
    expected = {"супермаркет": 0, "перевод": 0, "жкх": 0, "магазин": 0}
    assert result == expected


def test_missing_categories(sample_data):
    categories = ["кафе", "ресторан"]
    result = process_bank_operations(sample_data, categories)
    expected = {"кафе": 0, "ресторан": 0}
    assert result == expected


def test_partial_match(sample_data):
    categories = ["перевод", "оплата"]
    result = process_bank_operations(sample_data, categories)
    expected = {"перевод": 2, "оплата": 3}
    assert result == expected


def test_case_insensitivity(sample_data, sample_categories):

    modified_data = [
        {"amount": 1000, "description": "оплата в СУПЕРМАРКЕТЕ"},
        {"amount": 500, "description": "ПЕРЕВОД на карту"},
        {"amount": 300, "description": "ОПЛАТА ЖКХ"},
    ]
    result = process_bank_operations(modified_data, sample_categories)
    expected = {"супермаркет": 1, "перевод": 1, "жкх": 1, "магазин": 0}
    assert result == expected


def test_duplicate_categories(sample_data):
    categories = ["супермаркет", "супермаркет", "перевод"]
    result = process_bank_operations(sample_data, categories)
    expected = {"супермаркет": 2, "перевод": 2}
    assert result == expected
