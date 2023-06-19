import unittest
from unittest.mock import MagicMock, patch
import requests
from collections import Counter
from my_code import (
    get_auth,
    count_auth,
    get_ratio_auth,
    get_github_apis,
    get_categories_and_auth
)


class TestMyCode(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            'count': 3,
            'entries': [
                {
                    'Auth': 'apiKey',
                    'Link': 'https://example.com',
                    'Category': 'Category1'
                },
                {
                    'Auth': '',
                    'Link': 'https://github.com',
                    'Category': 'Category2'
                },
                {
                    'Auth': 'bearer',
                    'Link': 'https://example.com',
                    'Category': 'Category1'
                }
            ]
        }

    def test_get_auth(self):
        data = self.sample_data
        expected_result = ['apiKey', '', 'bearer']
        result = get_auth(data)
        self.assertEqual(result, expected_result)

    def test_count_auth(self):
        auth_list = ['apiKey', '', 'bearer', 'bearer', 'apiKey']
        expected_result = Counter({'apiKey': 2, 'bearer': 2, '': 1})
        result = count_auth(auth_list)
        self.assertEqual(result, expected_result)

    def test_get_ratio_auth(self):
        count_auth_types = Counter({'apiKey': 2, 'bearer': 2, '': 1})
        data = {'count': 5}
        expected_result = [
            'apiKey: 0.4000',
            'bearer: 0.4000',
            'Without Auth: 0.2000'
        ]
        result = get_ratio_auth(count_auth_types, data)
        self.assertEqual(result, expected_result)

    def test_get_github_apis(self):
        data = self.sample_data
        expected_result = 1
        result = get_github_apis(data)
        self.assertEqual(result, expected_result)

    def test_get_categories_and_auth(self):
        data = self.sample_data
        expected_result = {'Category1': 2, 'Category2': 1}
        result = get_categories_and_auth(data)
        self.assertEqual(result, expected_result)

    @patch('requests.get')
    def test_main_function_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.sample_data
        mock_get.return_value = mock_response

        expected_output = [
            'apiKey: 0.4000',
            'bearer: 0.4000',
            'Without Auth: 0.2000'
        ]

        with patch('builtins.print') as mock_print:
            import my_code
            my_code.main()
            mock_print.assert_called_with(expected_output)

    @patch('requests.get')
    def test_main_function_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        expected_output = 'Что-то пошло не так, код ошибки: 404'

        with patch('builtins.print') as mock_print:
            import my_code
            my_code.main()
            mock_print.assert_called_with(expected_output)


if __name__ == '__main__':
    unittest.main()
