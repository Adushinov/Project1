import unittest
from unittest.mock import MagicMock, patch

from external_api.currency_converter import CurrencyConverter
from src.transaction_processor import process_transaction


class TestTransactionProcessor(unittest.TestCase):
    @patch("external_api.currency_converter.CurrencyConverter.get_exchange_rate")
    def test_convert_usd(self, mock_get_rate):
        mock_get_rate.return_value = 75.0  # Примерный курс USD к RUB
        transaction = {"amount": 100, "currency": "USD"}
        result = process_transaction(transaction)
        self.assertEqual(result, 7500.0)

    @patch("external_api.currency_converter.CurrencyConverter.get_exchange_rate")
    def test_convert_eur(self, mock_get_rate):
        mock_get_rate.return_value = 80.0  # Примерный курс EUR к RUB
        transaction = {"amount": 50, "currency": "EUR"}
        result = process_transaction(transaction)
        self.assertEqual(result, 4000.0)

    def test_convert_rub(self):
        transaction = {"amount": 1000, "currency": "RUB"}
        result = process_transaction(transaction)
        self.assertEqual(result, 1000.0)

    def test_invalid_transaction(self):
        with self.assertRaises(ValueError):
            process_transaction({"amount": 100})  # Отсутствует
