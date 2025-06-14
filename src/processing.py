from typing import Dict, List

from widget import get_date


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список словарей по значению ключа 'state'"""
    filtered_data = []

    for item in data:
        if "state" in item and item["state"] == state:
            filtered_data.append(item)

    return filtered_data


def sort_by_date(operations: list, ascending: bool = False) -> list:
    """Функция принимает список словарей с операциями и сортирует их по значению ключа 'date'.
    Поддерживает как сортировку по возрастанию, так и по убыванию."""
    return sorted(operations, key=get_date, reverse=not ascending)

