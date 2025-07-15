import unittest
from unittest.mock import patch, MagicMock
import requests
from src.transaction_processor import currency_converter, process_transaction


class TestCurrencyConverter(unittest.TestCase):
    @patch('requests.get')
    def test_currency_converter_success(self, mock_get):
        # Создаем мок ответа
        mock_response = MagicMock()
        mock_response.json.return_value = {'result': 123.45}
        mock_get.return_value = mock_response

        # Вызываем функцию
        result = currency_converter(100, 'USD')

        # Проверяем результат
        self.assertEqual(result, 123.45)
        mock_get.assert_called_once()

    @patch('requests.get')
    def test_currency_converter_error(self, mock_get):
        # Симулируем ошибку API
        mock_get.side_effect = requests.exceptions.RequestException('API error')

        with self.assertRaises(Exception):
            currency_converter(100, 'USD')

    @patch('requests.get')
    def test_currency_converter_no_result(self, mock_get):
        # Симулируем ответ без результата
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        result = currency_converter(100, 'USD')
        self.assertEqual(result, 0.0)


class TestProcessTransaction(unittest.TestCase):

    def test_process_transaction_rub(self):
        transaction = {
            'operationAmount': {
                'amount': 100,
                'currency': {'code': 'RUB'}
            }
        }

        result = process_transaction(transaction)
        self.assertEqual(result, 100.0)

    @patch('src.transaction_processor.currency_converter')  # замените your_module на реальное имя вашего файла
    def test_process_transaction_foreign(self, mock_converter):
        # Мокаем результат конвертации
        mock_converter.return_value = 123.45

        transaction = {
            'operationAmount': {
                'amount': 100,
                'currency': {'code': 'USD'}
            }
        }

        result = process_transaction(transaction)
        self.assertEqual(result, 123.45)
        mock_converter.assert_called_once_with(100, 'USD')

    def test_process_transaction_missing_fields(self):
        transaction = {
            'operationAmount': {
                'amount': 100
            }
        }

        with self.assertRaises(ValueError):
            process_transaction(transaction)

    def test_process_transaction_invalid_data(self):
        transaction = {
            'operationAmount': {
                'currency': {'code': 'USD'}
            }
        }

        with self.assertRaises(ValueError):
            process_transaction(transaction)


if __name__ == '__main__':
    unittest.main()
