import pytest
from src.widget import mask_account_card


# Фикстуры для тестовых данных
@pytest.fixture
def valid_card_input():
    return "Иван Иванов 1234567890123456"


@pytest.fixture
def valid_account_input():
    return "Петр Петров 1234567890"


@pytest.fixture
def invalid_non_digit_card_input():
    return "Анна Сидорова 123a567890123456"


@pytest.fixture
def short_account_input():
    return "Мария Иванова 123"


# Тесты
def test_valid_card_input(valid_card_input):
    result = mask_account_card(valid_card_input)
    assert (
        result == "Иван Иванов 1234 56** **** 3456"
    ), f"Ожидалось: Иван Иванов 1234 56** **** 3456, получено: {result}"


def test_valid_account_input(valid_account_input):
    result = mask_account_card(valid_account_input)
    assert result == "Петр Петров **7890", f"Ожидалось: Петр Петров **7890, получено: {result}"


def test_invalid_non_digit_card_input(invalid_non_digit_card_input):
    result = mask_account_card(invalid_non_digit_card_input)
    expected = "Анна Сидорова Ошибка: номер карты должен содержать только цифры"
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"


def test_short_account_input(short_account_input):
    result = mask_account_card(short_account_input)
    expected = "Мария Иванова Ошибка: номер счёта должен содержать минимум 4 цифры"
    assert result == expected, f"Ожидалось: {expected}, получено: {result}"
