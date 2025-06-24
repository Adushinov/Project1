from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_str: str) -> str:
    """Функция, обрабатывает информацтию о картах и счетах"""
    parts = input_str.split()
    name = " ".join(parts[:-1])
    number = parts[-1]

    if len(number) == 16:  # карта
        masked_number = get_mask_card_number(number)
    else:  # счет
        masked_number = get_mask_account(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Функция, принимает данные и возвращает в виде день.месяц.год"""
    try:

        date_part = date_string.split("T")[0]

        year, month, day = date_part.split("-")

        return f"{day}.{month}.{year}"

    except (IndexError, ValueError):
        return "Ошибка: неверный формат даты"
