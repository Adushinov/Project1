import unittest
from unittest.mock import patch, MagicMock
from src.utils import load_transactions

class TestLoadTransactions(unittest.TestCase):


    @patch('builtins.open')
    def test_incorrect_structure(self, mock_open):
        """Тестирование случая, когда файл содержит неправильное значение (не список)"""
        mock_file_handle = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file_handle
        mock_file_handle.read.return_value = '{"id": 1}'  # объект, а не список

        result = load_transactions("some/path")
        self.assertEqual(result, [])

    @patch('os.path.exists')
    def test_nonexistent_file(self, mock_exists):
        """Тестируем случай отсутствующего файла"""
        mock_exists.return_value = False
        result = load_transactions("non_existent_file.json")
        self.assertEqual(result, [])

    @patch('builtins.open')
    def test_json_decode_error(self, mock_open):
        """Тестируем ситуацию повреждения JSON-файла"""
        mock_file_handle = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file_handle
        mock_file_handle.read.return_value = '{invalid json}'

        result = load_transactions("some/path")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()