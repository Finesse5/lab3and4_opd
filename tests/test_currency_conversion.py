import unittest
from app import get_exchange_rate, convert_currency

class TestCurrencyConversion(unittest.TestCase):

    def test_get_exchange_rate(self):
        # Проверка для случая, когда курс валюты равен 1.0 (заглушка)
        self.assertEqual(get_exchange_rate('USD', 'GBP'), 1.0)

    def test_convert_currency(self):
        # Проверка конвертации 100 единиц валюты по курсу 1.5
        self.assertEqual(convert_currency(100, 1.5), 150)
        # Проверка конвертации 50 единиц валюты по курсу 0.75
        self.assertEqual(convert_currency(50, 0.75), 37.5)

if __name__ == '__main__':
    unittest.main()
