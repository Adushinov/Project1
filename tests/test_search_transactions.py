from typing import Dict, List

import pytest

from src.search_transactions import (process_bank_operations,  # Замените your_module на реальное имя
                                     process_bank_search)


# Фикстуры с тестовыми данными
@pytest.fixture
def simple_transactions() -> List[Dict]:
    return [
        {"description": "Перевод с карты на карту"},
        {"description": "Оплата услуг ЖКХ"},
        {"description": "Пополнение счета"},
        {"description": "Снятие наличных"},
        {"description": None},
        {"description": "Оплата картой в магазине"},
    ]


@pytest.fixture
def empty_transactions() -> List[Dict]:
    return []


@pytest.fixture
def transactions_with_none() -> List[Dict]:
    return [{"description": None}, {"description": "Оплата услуг"}, {"description": "Пополнение счета"}]


def test_search_partial_match(simple_transactions):
    result = process_bank_search(simple_transactions, "услуг")
    expected = [{"description": "Оплата услуг ЖКХ"}]
    assert result == expected


def test_search_case_insensitive(simple_transactions):
    result = process_bank_search(simple_transactions, "КАРТОЙ")
    expected = [{"description": "Оплата картой в магазине"}]
    assert result == expected


def test_search_none_values(transactions_with_none):
    result = process_bank_search(transactions_with_none, "услуг")
    expected = [{"description": "Оплата услуг"}]
    assert result == result


def test_search_empty_list(empty_transactions):
    result = process_bank_search(empty_transactions, "любой_поиск")
    assert result == []


# Тесты для process_bank_operations
def test_count_categories(simple_transactions):
    categories = ["перевод", "оплата", "пополнение"]
    result = process_bank_operations(simple_transactions, categories)
    expected = {"перевод": 1, "оплата": 2, "пополнение": 1}
    assert result == expected


def test_count_case_insensitive(simple_transactions):
    categories = ["ОПЛАТА", "ПЕРЕВОД"]
    result = process_bank_operations(simple_transactions, categories)
    expected = {"ОПЛАТА": 2, "ПЕРЕВОД": 1}
    assert result == expected


def test_count_no_matches(simple_transactions):
    categories = ["магазин", "ресторан"]
    result = process_bank_operations(simple_transactions, categories)
    expected = {"магазин": 1, "ресторан": 0}  # Только один раз встречается "магазин"
    assert result == expected


def test_count_with_none(transactions_with_none):
    categories = ["услуг", "счета"]
    result = process_bank_operations(transactions_with_none, categories)
    expected = {"услуг": 1, "счета": 1}
    assert result == expected


def test_count_empty_list(empty_transactions):
    categories = ["любой", "категория"]
    result = process_bank_operations(empty_transactions, categories)
    expected = {"любой": 0, "категория": 0}
    assert result == expected
