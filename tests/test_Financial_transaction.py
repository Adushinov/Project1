from unittest.mock import Mock, patch

import pandas as pd
import pytest

from src.Financial_transaction import read_excel_transactions, read_transactions

TEST_EXCEL_DATA = {"id": [1, 2], "amount": [100.00, 200.00], "date": ["2025-07-20", "2025-07-21"]}


# Тест для функции read_transactions
def test_read_transactions():
    with patch("pandas.read_csv") as mock_read_csv:
        mock_df = pd.DataFrame({"id": [1, 2], "amount": [100.00, 200.00], "date": ["2025-07-20", "2025-07-21"]})
        mock_read_csv.return_value = mock_df
        result = read_transactions("dummy_path.csv")

        expected_result = [
            {"id": 1, "amount": 100.00, "date": "2025-07-20"},
            {"id": 2, "amount": 200.00, "date": "2025-07-21"},
        ]
        assert result == expected_result
        mock_read_csv.assert_called_once_with("dummy_path.csv")


# Тест для функции read_excel_transactions
def test_read_excel_transactions():

    with patch("pandas.read_excel") as mock_read_excel:

        mock_df = pd.DataFrame(TEST_EXCEL_DATA)

        mock_read_excel.return_value = mock_df

        result = read_excel_transactions("dummy_path.xlsx")

        expected_result = [
            {"id": 1, "amount": 100.00, "date": "2025-07-20"},
            {"id": 2, "amount": 200.00, "date": "2025-07-21"},
        ]
        assert result == expected_result
        mock_read_excel.assert_called_once_with("dummy_path.xlsx", engine="openpyxl")


def test_read_transactions_error():
    with patch("pandas.read_csv") as mock_read_csv:
        mock_read_csv.side_effect = FileNotFoundError
        with pytest.raises(FileNotFoundError):
            read_transactions("non_existent_file.csv")


def test_read_excel_transactions_error():
    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.side_effect = FileNotFoundError
        with pytest.raises(FileNotFoundError):
            read_excel_transactions("non_existent_file.xlsx")
