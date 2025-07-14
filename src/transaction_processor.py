from external_api.currency_converter import CurrencyConverter


def process_transaction(transaction: dict) -> float:
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if not amount or not currency:
        raise ValueError("Transaction must contain 'amount' and 'currency' fields")

    return CurrencyConverter.convert_to_rub(amount, currency)
