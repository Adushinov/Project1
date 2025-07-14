import os
import requests
from dotenv import load_dotenv

load_dotenv()

class CurrencyConverter:
    BASE_URL = "https://api.exchangerate-api.com/v4/latest/{base_currency}"
    API_KEY = os.getenv("EXCHANGE_API_KEY")
    BASE_CURRENCY = "RUB"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "apikey": self.API_KEY
        })

    def get_exchange_rate(self, currency: str) -> float:
        try:
            response = self.session.get(
                self.API_URL,
                params={
                    "access_key": self.API_KEY,
                    "symbols": currency,
                    "format": 1
                }
            )
            response.raise_for_status()
            data = response.json()
            return data["rates"][currency]
        except requests.RequestException as e:
            raise Exception(f"Ошибка при получении курса валют: {str(e)}")
        except KeyError:
            raise Exception("Неверный формат ответа от API")

    def convert_to_rub(self, amount: float, currency: str) -> float:
        if currency == "RUB":
            return amount
        rate = self.get_exchange_rate(currency)
        return amount * rate
