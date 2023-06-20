import requests
import unittest
from unittest.mock import Mock, patch

class TestCalculateWorkingHours(unittest.TestCase):
    def test_calculate_working_hours(self):
        # Заглушка для requests.get()
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "1": 8,
            "2": 8,
            "3": 6,
            "4": 0,
            "5": 8
        }
        
        # Имитация запроса к API
        with patch('requests.get', return_value=mock_response) as mock_get:
            months = [1, 2, 3, 4, 5]
            result = calculate_working_hours(months)
            
            # Проверка результата
            self.assertEqual(result, 30)
            
            # Проверка вызова requests.get()
            expected_url = "https://example.com/api/working_hours/1"
            mock_get.assert_called_with(expected_url)
            
            # Проверка вызова response.json()
            mock_response.json.assert_called_once()
            
if __name__ == '__main__':
    unittest.main()
