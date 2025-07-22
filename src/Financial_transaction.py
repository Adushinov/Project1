import pandas as pd


def read_transactions(csv_path):
    """функция для считывания финансовых операций из CSV."""
    df = pd.read_csv(csv_path)
    transactions = df.to_dict(orient="records")
    return transactions


def read_excel_transactions(excel_path):
    """функция для считывания финансовых операций из Excel."""
    df = pd.read_excel(excel_path, engine="openpyxl")
    transactions = df.to_dict(orient="records")
    return transactions
