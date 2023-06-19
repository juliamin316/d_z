import unittest
from unittest.mock import patch
from currency_converter import (
    get_value_and_currency,
    request,
    find_price,
    convert
)


class CurrencyConverterTest(unittest.TestCase):
    @patch('currency_converter.requests.get')
    def test_get_value_and_currency(self, mock_get):
        input_data = "100 RUB"
        expected_value = "100"
        expected_currency = "RUB"
        value, currency = get_value_and_currency(input_data)
        self.assertEqual(value, expected_value)
        self.assertEqual(currency, expected_currency)

    @patch('currency_converter.requests.get')
    def test_request(self, mock_get):
        mock_get.return_value.json.return_value = {"rates": {"USD": 0.012}}
        convert_currency = "USD"
        expected_url = "https://open.er-api.com/v6/latest/USD"
        response = request(convert_currency)
        mock_get.assert_called_once_with(expected_url)
        self.assertEqual(response, {"rates": {"USD": 0.012}})

    def test_find_price(self):
        data = {"rates": {"RUB": 80.0, "USD": 1.0}}
        local_currency = "RUB"
        convert_currency = "USD"
        expected_price = 1.0
        price = find_price(data, local_currency, convert_currency)
        self.assertEqual(price, expected_price)

    def test_convert(self):
        value = 100.0
        price = 0.012
        local_currency = "RUB"
        convert_currency = "USD"
        expected_result = "Ваши 100.0 RUB это 8333.33 USD"
        result = convert(value, price, local_currency, convert_currency)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
