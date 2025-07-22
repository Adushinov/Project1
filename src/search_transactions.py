import re
from collections import Counter
from typing import Dict, List


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Функция поиска операций по описанию с использованием регулярных выражений.
    """

    pattern = re.compile(rf"\b{re.escape(search)}\b", re.IGNORECASE)

    result = [
        operation
        for operation in data
        if operation.get("description") is not None and pattern.search(operation.get("description"))
    ]

    return result


def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Функция для подсчета количества операций по заданным категориям
    с использованием Counter для оптимизации подсчета.
    """

    counter = Counter()

    categories_set = set(category.lower() for category in categories)

    for operation in data:
        description = operation.get("description", "").lower()

        for category in categories_set:
            if category in description:
                counter[category.capitalize()] += 1
                break

    return {category: counter.get(category.capitalize(), 0) for category in categories}
