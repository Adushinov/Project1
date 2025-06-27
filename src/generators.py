from typing import Iterator, Dict, Any

def filter_by_currency(transactions: list[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по заданной валюте и возвращает итератор"""

    def transactions_filter() -> Iterator[Dict[str, Any]]:
        for transaction in transactions:
            if ('operationAmount' in transaction
                and 'currency' in transaction['operationAmount']
                and transaction['operationAmount']['currency'].get('code') == currency):
                yield transaction

    return transactions_filter()


from typing import Generator, Dict, Any


def transaction_descriptions(transactions: list[Dict[str, Any]]) -> Generator[str, None, None]:
    """Генератор, последовательно возвращающий описание транзакций"""
    for transaction in transactions:
        desc = transaction.get('description')
        yield desc if desc is not None else "Нет описания"


def card_number_generator(start: int, end: int) -> str:
    """Генератор номеров банковских карт в заданном диапазоне"""
    if start < 1 or end > 9999999999999999 or start > end:
        raise ValueError('Диапазон должен быть от 1 до 9999999999999999, start <= end')

    for num in range(start, end + 1):
        card_str = f'{num:016d}'
        yield ' '.join(card_str[i:i+4] for i in range(0, 16, 4))
