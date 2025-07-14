import json
import os


def load_transactions(file_path):
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            transactions = json.load(f)

        if isinstance(transactions, list):
            return transactions
        else:
            return []

    except json.JSONDecodeError:
        return []
