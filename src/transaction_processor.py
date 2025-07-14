from external_api.currency_converter import CurrencyConverter


def process_transaction(transaction: dict) -> float:
    """
    Обрабатывает транзакцию и возвращает сумму в рублях
    :param transaction: словарь с полями 'amount' и 'currency'
    :return: сумма в рублях (float)
    """
    converter = CurrencyConverter()
    amount = transaction.get("amount")
    currency = transaction.get("currency")

    if not amount or not currency:
        raise ValueError("Транзакция должна содержать поля 'amount' и 'currency'")

    return converter.convert_to_rub(amount, currency)
