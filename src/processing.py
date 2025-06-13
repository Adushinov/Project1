from typing import Dict, List

from widget import get_date


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список словарей по значению ключа 'state'"""
    filtered_data = []

    for item in data:
        if "state" in item and item["state"] == state:
            filtered_data.append(item)

    return filtered_data

