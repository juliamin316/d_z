import unittest
from unittest.mock import MagicMock
import requests
from your_module import get_joke_types


class TestGetJokeTypes(unittest.TestCase):
    def setUp(self):
        self.url = 'https://official-joke-api.appspot.com/jokes/ten'

    def test_get_joke_types_success(self):
        # Создание mock-объекта для имитации успешного запроса
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {'type': 'type1'},
            {'type': 'type2'},
            {'type': 'type3'}
        ]
        requests.get = MagicMock(return_value=mock_response)

        expected_result = ['type1', 'type2', 'type3']
        result = get_joke_types(self.url)

        self.assertEqual(result, expected_result)
        requests.get.assert_called_once_with(self.url)

    def test_get_joke_types_error(self):
        # Создание mock-объекта для имитации ошибки при запросе
        mock_response = MagicMock()
        mock_response.status_code = 404
        requests.get = MagicMock(return_value=mock_response)

        result = get_joke_types(self.url)

        self.assertEqual(result, [])
        requests.get.assert_called_once_with(self.url)
        print.assert_called_once_with("Error: 404")


if __name__ == '__main__':
    unittest.main()
