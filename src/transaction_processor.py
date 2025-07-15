import os
import requests

def currency_converter(amount: float, currency_from: str, currency_to: str = "RUB") -> float:
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": os.getenv("EXCHANGE_API_KEY")}
    params = {"amount": amount, "from": currency_from, "to": currency_to}

    response = requests.get(url, headers=headers, params=params).json()
    return float(response.get("result", 0))

def process_transaction(transaction: dict) -> float:
    """
    Обрабатывает транзакцию и возвращает сумму в рублях
    :param transaction: словарь с полями 'amount' и 'currency'
    :return: сумма в рублях (float)
    """
    amount = transaction.get("operationAmount", {}).get("amount")
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if not amount or not currency:
        raise ValueError("Транзакция должна содержать поля 'amount' и 'currency'")

    if currency == "RUB":
        return float(amount)
    else:
        return currency_converter(amount, currency)