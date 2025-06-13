def get_mask_card_number(card_number: str) -> str:
    """Функция, принимает номер карты и маскирует его"""
    if not card_number.isdigit():
        return "Ошибка: номер карты должен содержать только цифры"

    if len(card_number) != 16:
        return "Ошибка: номер карты должен содержать 16 цифр"

    first_part = card_number[0:4]
    second_part = card_number[4:8]
    fourth_part = card_number[12:16]

    second_part_masked = second_part[0:2] + "**"

    third_part_masked = "****"

    masked_number = f"{first_part} {second_part_masked} {third_part_masked} {fourth_part}"

    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    if not account_number.isdigit():
        return "Ошибка: номер карты должен состоять только из цифры"

    if len(account_number) < 4:
        return "Ошибка: номер счета должен содержать минимум 4 цифры"

    masked_number = "**{}".format(account_number[-4:])

    return masked_number
