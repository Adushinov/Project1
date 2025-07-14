import unittest
from unittest.mock import patch, MagicMock
from src.transaction_processor import process_transaction


class TestTransactionProcessor(unittest.TestCase):
    @patch('external_api.currency_converter.CurrencyConverter.get_exchange_rate')
    def test_process_transaction_usd(self, mock_get_rate):
        mock_get_rate.return_value = 75.0  # Примерный курс USD к RUB

        transaction = {
            'amount': 100.0,
            'currency': 'USD'
        }

        result = process_transaction(transaction)
        self.assertEqual(result, 7500.0)

    @patch('external_api.currency_converter.CurrencyConverter.get_exchange_rate')
    def test_process_transaction_eur(self, mock_get_rate):
        mock_get_rate.return_value = 85.0  # Примерный курс EUR к RUB

        transaction = {
            'amount': 50.0,
            'currency': 'EUR'
        }

        result = process_transaction(transaction)
        self.assertEqual(result, 4250.0)

    def test_process_transaction_rub(self):
        transaction = {
            'amount': 1000.0,
            'currency': 'RUB'
        }

        result = process_transaction(transaction)
        self.assertEqual(result, 1000.0)

    def test_missing_fields(self):
        with self.assertRaises(ValueError):
            process_transaction({'amount': 100.0})

        with self.assertRaises(ValueError):
            process_transaction({'currency': 'USD'})


if __name__ == '__main__':
    unittest.main()
