import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("123a567890123456", "Ошибка: номер карты должен содержать только цифры"),
        ("12345678", "Ошибка: номер карты должен содержать 16 цифр"),
        ("12345678901234567", "Ошибка: номер карты должен содержать 16 цифр"),
    ],
)
def test_card_masking(card, expected):
    result = get_mask_card_number(card)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


@pytest.fixture
def valid_card():
    return "1234567890123456"


@pytest.fixture
def invalid_non_digit_card():
    return "123a567890123456"


@pytest.fixture
def short_card():
    return "12345678"


@pytest.fixture
def long_card():
    return "12345678901234567"


# Тесты
def test_valid_card(valid_card):
    result = get_mask_card_number(valid_card)
    assert result == "1234 56** **** 3456", f"Ожидалось: 1234 56** **** 3456, получено: {result}"


def test_invalid_non_digit_card(invalid_non_digit_card):
    result = get_mask_card_number(invalid_non_digit_card)
    expected = "Ошибка: номер карты должен содержать только цифры"
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


def test_short_card(short_card):
    result = get_mask_card_number(short_card)
    expected = "Ошибка: номер карты должен содержать 16 цифр"
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


def test_long_card(long_card):
    result = get_mask_card_number(long_card)
    expected = "Ошибка: номер карты должен содержать 16 цифр"
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


import pytest


@pytest.mark.parametrize(
    "account, expected",
    [
        ("1234567890123456", "**3456"),
        ("123a456", "Ошибка: номер счёта должен состоять только из цифры"),
        ("123", "Ошибка: номер счёта должен содержать минимум 4 цифры"),
    ],
)
def test_account_masking(account, expected):
    result = get_mask_account(account)
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


@pytest.fixture
def valid_account():
    return "1234567890123456"


@pytest.fixture
def invalid_non_digit_account():
    return "123a456"


@pytest.fixture
def short_account():
    return "123"


# Тесты
def test_valid_account(valid_account):
    result = get_mask_account(valid_account)
    assert result == "**3456", f"Ожидалось: **3456, получено: {result}"


def test_invalid_non_digit_account(invalid_non_digit_account):
    result = get_mask_account(invalid_non_digit_account)
    expected = "Ошибка: номер счёта должен состоять только из цифры"
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


def test_short_account(short_account):
    result = get_mask_account(short_account)
    expected = "Ошибка: номер счёта должен содержать минимум 4 цифры"
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"



