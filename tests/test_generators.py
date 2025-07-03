from typing import Any, Dict, Generator, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions() -> list[Dict[str, Any]]:
    return [
        {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"amount": "200", "currency": {"code": "EUR"}}},
        {"id": 3, "operationAmount": {"amount": "300", "currency": {"code": "USD"}}},
        {"id": 4, "operationAmount": {"amount": "400"}},
        {"id": 5, "description": "Invalid transaction"},
    ]


@pytest.mark.parametrize("currency, expected_ids", [("USD", [1, 3]), ("EUR", [2]), ("GBP", []), ("RUB", [])])
def test_filter_by_currency_valid_cases(sample_transactions, currency, expected_ids):

    result = filter_by_currency(sample_transactions, currency)

    assert [t["id"] for t in result] == expected_ids


def test_filter_with_invalid_transactions(sample_transactions):

    currency = "USD"

    result = list(filter_by_currency(sample_transactions, currency))

    assert len(result) == 2
    assert all(t["id"] in {1, 3} for t in result)


def test_empty_input():

    transactions = []
    currency = "USD"

    result = list(filter_by_currency(transactions, currency))

    assert len(result) == 0


def test_iterator_behavior(sample_transactions):

    currency = "USD"

    iterator = filter_by_currency(sample_transactions, currency)

    assert next(iterator)["id"] == 1
    assert next(iterator)["id"] == 3

    with pytest.raises(StopIteration):
        next(iterator)


@pytest.mark.parametrize(
    "invalid_transaction",
    [
        {"operationAmount": {"currency": {"code": 123}}},
        {"operationAmount": {"currency": {"code": None}}},
        {"operationAmount": {"currency": {}}},
    ],
)
def test_invalid_currency_codes(invalid_transaction):

    transactions = [invalid_transaction]
    currency = "USD"

    result = list(filter_by_currency(transactions, currency))

    assert len(result) == 0


test_cases = [
    (
        [{"description": "Покупка в магазине"}, {"description": "Перевод средств"}],
        ["Покупка в магазине", "Перевод средств"],
    ),
    ([{"description": None}, {}, {"description": "Оплата услуг"}], ["Нет описания", "Нет описания", "Оплата услуг"]),
    ([], []),
]


@pytest.mark.parametrize("transactions, expected", test_cases)
def test_transaction_descriptions(transactions: List[Dict[str, Any]], expected: List[str]):
    result = list(transaction_descriptions(transactions))
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


test_cases = [
    (1, 1, ["0000 0000 0000 0001"]),
    (9999, 9999, ["0000 0000 0009 9999"]),
    (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
    (1000, 1002, ["0000 0000 0100 0000", "0000 0000 0100 0001", "0000 0000 0100 0002"]),
]


test_cases = [
    (1, 1, ["0000 0000 0000 0001"]),
    (9999, 9999, ["0000 0000 0000 9999"]),
    (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
    (1000, 1002, ["0000 0000 0100 0000", "0000 0000 0100 0001", "0000 0000 0100 0002"]),
]

test_cases = [
    (1, 1, ["0000 0000 0000 0001"]),
    (9999, 9999, ["0000 0000 0000 9999"]),  # Исправленное ожидаемое значение
    (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
    (
        1000,
        1002,
        ["0000 0000 0000 1000", "0000 0000 0000 1001", "0000 0000 0000 1002"],
    ),  # Исправленные ожидаемые значения
]


@pytest.mark.parametrize("start, end, expected", test_cases)
def test_card_number_generator(start: int, end: int, expected: List[str]):
    result = list(card_number_generator(start, end))
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


def test_invalid_range():
    with pytest.raises(ValueError):
        list(card_number_generator(0, 1))
    with pytest.raises(ValueError):
        list(card_number_generator(10000000000000000, 10000000000000001))
    with pytest.raises(ValueError):
        list(card_number_generator(5, 1))
