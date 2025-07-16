import logging
import os

# Создаем директорию для логов
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Создаем отдельный логгер для модуля masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)  # Устанавливаем уровень не ниже DEBUG

# Создаем обработчик для записи в файл
file_handler = logging.FileHandler(os.path.join(log_dir, "masks.log"))
file_handler.setLevel(logging.DEBUG)

# Создаем обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Форматировщик для логов
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Применяем форматировщик
file_handler.setFormatter(file_formatter)
console_handler.setFormatter(file_formatter)

# Добавляем обработчики к логгеру
masks_logger.addHandler(file_handler)
masks_logger.addHandler(console_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, принимает номер карты и маскирует его"""
    try:
        if not card_number.isdigit():
            logging.error(f"Ошибка валидации номера карты: {card_number}. Номер содержит нецифровые символы")
            return "Ошибка: номер карты должен содержать только цифры"

        if len(card_number) != 16:
            logging.error(f"Ошибка валидации номера карты: {card_number}. Неверная длина")
            return "Ошибка: номер карты должен содержать 16 цифр"

        first_part = card_number[0:4]
        second_part = card_number[4:8]
        fourth_part = card_number[12:16]

        second_part_masked = second_part[0:2] + "**"
        third_part_masked = "****"

        masked_number = f"{first_part} {second_part_masked} {third_part_masked} {fourth_part}"
        logging.info(f"Успешная маскировка карты: {masked_number}")
        return masked_number

    except Exception as e:
        logging.exception(f"Непредвиденная ошибка при обработке карты: {card_number}")
        return "Произошла ошибка при обработке карты"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    try:
        if not account_number.isdigit():
            logging.error(f"Ошибка валидации номера счета: {account_number}. Номер содержит нецифровые символы")
            return "Ошибка: номер счёта должен состоять только из цифры"

        if len(account_number) < 4:
            logging.error(f"Ошибка валидации номера счета: {account_number}. Неверная длина")
            return "Ошибка: номер счёта должен содержать минимум 4 цифры"

        masked_number = "**{}".format(account_number[-4:])
        logging.info(f"Успешная маскировка счета: {masked_number}")
        return masked_number

    except Exception as e:
        logging.exception(f"Непредвиденная ошибка при обработке счета: {account_number}")
        return "Произошла ошибка при обработке счета"


# Пример использования
if __name__ == "__main__":
    # Тестовые случаи для маскировки карты
    masks_logger.info("Запуск тестов для маскировки карт")

    # Корректные тестовые данные
    test_cards = [
        "1234567890123456",  # корректная карта
        "1234-5678-9012-3456",  # некорректные символы
        "123456789012345",  # неверная длина
        "12345678901234567",  # слишком длинная
        "1234a56789012345",  # буквенные символы
        "1234 5678 9012 3456",  # пробелы
    ]

    for card in test_cards:
        result = get_mask_card_number(card)
        masks_logger.debug(f"Тест карты {card}: результат - {result}")
        print(f"Карта {card} -> {result}")

    # Тестовые случаи для маскировки счета
    masks_logger.info("Запуск тестов для маскировки счетов")

    # Корректные тестовые данные
    test_accounts = [
        "1234567890123456",  # корректный счет
        "1234",  # минимальная длина
        "123",  # слишком короткий
        "1234abc567",  # буквенные символы
        "12345678901234567890",  # длинный счет
        " 1234567890123456 ",  # с пробелами
    ]

    for account in test_accounts:
        result = get_mask_account(account)
        masks_logger.debug(f"Тест счета {account}: результат - {result}")
        print(f"Счет {account} -> {result}")

    masks_logger.info("Тестирование завершено")
