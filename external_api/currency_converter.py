import os
import requests
from dotenv import load_dotenv

load_dotenv()


class CurrencyConverter:
    API_URL = "https://api.exchangeratesapi.io/v1/latest"
    ACCESS_KEY = os.getenv("EXCHANGE_RATES_API_KEY")

    @staticmethod
    def get_exchange_rate(currency: str) -> float:
        params = {
            'access_key': CurrencyConverter.ACCESS_KEY,
            'symbols': currency,
            'format': 1
        }

        response = requests.get(CurrencyConverter.API_URL, params=params)
        response.raise_for_status()

        data = response.json()
        return data['rates'][currency]

    @staticmethod
    def convert_to_rub(amount: float, currency: str) -> float:
        if currency == 'RUB':
            return amount

        rate = CurrencyConverter.get_exchange_rate(currency)
        return amount * rate



