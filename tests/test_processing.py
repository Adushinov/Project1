from datetime import datetime
from typing import Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "data, expected_length, expected_state",
    [
        (
            [
                {"id": 1, "state": "EXECUTED", "date": datetime(2023, 1, 1)},
                {"id": 3, "state": "EXECUTED", "date": datetime(2023, 1, 3)},
            ],
            2,
            "EXECUTED",
        ),
        (
            [
                {"id": 1, "date": datetime(2023, 1, 6)},
                {"id": 2, "state": "EXECUTED", "date": datetime(2023, 1, 7)},
                {"id": 3, "date": datetime(2023, 1, 8)},
            ],
            1,
            "EXECUTED",
        ),
        ([], 0, None),
    ],
)
def test_filter_by_state(data, expected_length, expected_state):
    result = filter_by_state(data)
    assert len(result) == expected_length
    if expected_state:
        assert all(item["state"] == expected_state for item in result)


@pytest.fixture
def valid_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": datetime(2023, 1, 1)},
        {"id": 3, "state": "EXECUTED", "date": datetime(2023, 1, 3)},
    ]


@pytest.fixture
def data_with_other_state():
    return [
        {"id": 1, "state": "CANCELLED", "date": datetime(2023, 1, 4)},
        {"id": 2, "state": "FAILED", "date": datetime(2023, 1, 5)},
    ]


@pytest.fixture
def data_without_state():
    return [
        {"id": 1, "date": datetime(2023, 1, 6)},
        {"id": 2, "state": "EXECUTED", "date": datetime(2023, 1, 7)},
        {"id": 3, "date": datetime(2023, 1, 8)},
    ]


@pytest.fixture
def empty_data():
    return []


# Тесты
def test_filter_by_default_state(valid_data):
    result = filter_by_state(valid_data)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_missing_state_key(data_without_state):
    result = filter_by_state(data_without_state)
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_empty_data(empty_data):
    result = filter_by_state(empty_data)
    assert result == []



# Фикстура для тестовых данных
@pytest.fixture
def sample_operations():
    return [
        {
            "id": 1,
            "date": "2023-01-01T00:00:00.000000",
            "state": "EXECUTED"
        },
        {
            "id": 2,
            "date": "2023-03-15T12:34:56.789000",
            "state": "EXECUTED"
        },
        {
            "id": 3,
            "date": "2023-02-01T00:00:00.000000",
            "state": "EXECUTED"
        }
    ]


# Базовый тест на сортировку по возрастанию
def test_sort_ascending(sample_operations):
    sorted_ops = sort_by_date(sample_operations, ascending=True)
    expected_dates = [
        "2023-01-01T00:00:00.000000",
        "2023-02-01T00:00:00.000000",
        "2023-03-15T12:34:56.789000"
    ]

    assert [op["date"] for op in sorted_ops] == expected_dates


# Тест на сортировку по убыванию
def test_sort_descending(sample_operations):
    sorted_ops = sort_by_date(sample_operations, ascending=False)
    expected_dates = [
        "2023-03-15T12:34:56.789000",
        "2023-02-01T00:00:00.000000",
        "2023-01-01T00:00:00.000000"
    ]

    assert [op["date"] for op in sorted_ops] == expected_dates


# Тест с пустыми данными
def test_empty_list():
    result = sort_by_date([])
    assert result == []


# Тест с одной операцией
def test_single_operation():
    single_op = [
        {
            "id": 1,
            "date": "2023-01-01T00:00:00.000000",
            "state": "EXECUTED"
        }
    ]
    result = sort_by_date(single_op)
    assert result == single_op


# Тест с отсутствующим ключом date
def test_missing_date_key():
    invalid_ops = [
        {
            "id": 1,
            "state": "EXECUTED"
        }
    ]
    with pytest.raises(ValueError):
        sort_by_date(invalid_ops)


# Тест с некорректным форматом даты
def test_invalid_date_format():
    invalid_ops = [
        {
            "id": 1,
            "date": "2023-01-01",  # Неверный формат
            "state": "EXECUTED"
        }
    ]
    with pytest.raises(ValueError):
        sort_by_date(invalid_ops)



