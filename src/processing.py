from typing import List, Dict
from datetime import datetime

def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список словарей по значению ключа 'state'"""
    filtered_data = []

    for item in data:
        if "state" in item and item["state"] == state:
            filtered_data.append(item)

    return filtered_data

def sort_by_date(operations: List[Dict], ascending: bool = False) -> List[Dict]:
    """Сортирует список операций по дате."""

    def get_date(operation: Dict) -> datetime:
        try:
            date_string: str = operation["date"]
            # Преобразуем строку в объект datetime для корректной сортировки
            return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
        except (KeyError, ValueError):
            raise ValueError("Некорректный формат даты или отсутствие ключа 'date'")

    # Сортируем список с использованием полученной функции get_date
    return sorted(operations, key=get_date, reverse=not ascending)