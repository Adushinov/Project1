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
    assert len(result) != 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_missing_state_key(data_without_state):
    result = filter_by_state(data_without_state)
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_empty_data(empty_data):
    result = filter_by_state(empty_data)
    assert result == []


@pytest.mark.parametrize(
    "data, ascending, expected_dates",
    [
        (
            [
                {"id": 1, "date": "2023-01-01T12:00:00.000"},
                {"id": 2, "date": "2023-01-03T12:00:00.000"},
                {"id": 3, "date": "2023-01-02T12:00:00.000"},
            ],
            True,
            ["2023-01-01T12:00:00.000", "2023-01-02T12:00:00.000", "2023-01-03T12:00:00.000"],
        ),
        (
            [
                {"id": 1, "date": "2023-01-01T12:00:00.000"},
                {"id": 2, "date": "2023-01-03T12:00:00.000"},
                {"id": 3, "date": "2023-01-02T12:00:00.000"},
            ],
            False,
            ["2023-01-03T12:00:00.000", "2023-01-02T12:00:00.000", "2023-01-01T12:00:00.000"],
        ),
    ],
)
def test_sort_by_date(data, ascending, expected_dates):
    result = sort_by_date(data, ascending=ascending)
    assert [item["date"] for item in result] == expected_dates


@pytest.fixture
def valid_data():
    return [
        {"id": 1, "date": "2023-01-01T12:00:00.000"},
        {"id": 2, "date": "2023-01-03T12:00:00.000"},
        {"id": 3, "date": "2023-01-02T12:00:00.000"},
    ]


@pytest.fixture
def data_with_incorrect_date():
    return [{"id": 1, "date": "invalid-date"}, {"id": 2, "date": "2023-01-02T12:00:00.000"}]


@pytest.fixture
def data_without_date_key():
    return [{"id": 1}, {"id": 2, "date": "2023-01-02T12:00:00.000"}]


@pytest.fixture
def empty_data():
    return []


# Тесты
def test_sort_by_ascending(valid_data):
    result = sort_by_date(valid_data, ascending=True)
    expected_dates = ["2023-01-01T12:00:00.000", "2023-01-02T12:00:00.000", "2023-01-03T12:00:00.000"]
    assert [item["date"] for item in result] == expected_dates


def test_sort_by_descending(valid_data):
    result = sort_by_date(valid_data, ascending=False)
    expected_dates = ["2023-01-03T12:00:00.000", "2023-01-02T12:00:00.000", "2023-01-01T12:00:00.000"]
    assert [item["date"] for item in result] == expected_dates


def test_incorrect_date_format(data_with_incorrect_date):
    with pytest.raises(ValueError):
        sort_by_date(data_with_incorrect_date)


def test_missing_date_key(data_without_date_key):
    with pytest.raises(ValueError):
        sort_by_date(data_without_date_key)


def test_empty_data(empty_data):
    result = sort_by_date(empty_data)
    assert result == []
