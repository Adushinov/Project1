import json
import logging
import os
from datetime import datetime

# Настройка директории для логов
log_dir = "logs"
try:
    os.makedirs(log_dir, exist_ok=True)
    print(f"Директория {log_dir} создана успешно")
except Exception as e:
    print(f"Ошибка создания директории: {str(e)}")
    log_dir = "."  # Используем текущую директорию как запасной вариант

# Настройка логгера для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Устанавливаем минимальный уровень DEBUG

# Создаем файловый обработчик
file_handler = logging.FileHandler(os.path.join(log_dir, "utils.log"), mode="w")

# Настраиваем формат логов
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Применяем форматтер к обработчику
file_handler.setFormatter(file_formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)


def load_transactions(file_path):
    try:
        # Проверка существования файла
        if not os.path.exists(file_path):
            logging.warning(f"Файл не найден: {file_path}")
            return []

        # Попытка открыть и прочитать файл
        with open(file_path, "r", encoding="utf-8") as f:
            transactions = json.load(f)

        # Проверка корректности данных
        if isinstance(transactions, list):
            logging.info(f"Успешная загрузка транзакций из файла: {file_path}")
            return transactions
        else:
            logging.warning(f"Данные в файле {file_path} не являются списком")
            return []

    except json.JSONDecodeError:
        logging.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []

    except Exception as e:
        logging.error(f"Непредвиденная ошибка при работе с файлом {file_path}: {str(e)}")
        return []


# Тестовый вызов для проверки работы логирования
if __name__ == "__main__":
    logger.info("Программа запущена")
    load_transactions("test_file.json")
    logger.info("Программа завершила работу")
