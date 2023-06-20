import unittest
from unittest.mock import patch, Mock
from datetime import datetime
import requests


class TestContest(unittest.TestCase):
    def setUp(self):
        self.mock_response = {
            "key": "mock_site",
            "name": "Mock Site"
        }

        self.mock_contests = [
            {
                "name": "Contest 1",
                "start_time": "2023-06-30T10:00:00+05:30"
            },
            {
                "name": "Contest 2",
                "start_time": "23-06-30"
            },
            {
                "name": "Contest 3",
                "start_time": "2022-12-31T00:00:00+00:00"
            }
        ]

    def test_get_sites_success(self):
        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = [self.mock_response]
            mock_get.return_value = mock_response

            from kontests import get_sites

            sites = get_sites("https://kontests.net/api/v1/sites")
            mock_get.assert_called_once_with("https://kontests.net/api/v1/sites")
            self.assertEqual(sites, [self.mock_response])

    def test_get_sites_failure(self):
        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response

            from kontests import get_sites

            with self.assertRaises(Exception) as context:
                get_sites("https://kontests.net/api/v1/sites")

            mock_get.assert_called_once_with("https://kontests.net/api/v1/sites")
            self.assertEqual(str(context.exception), "Что-то пошло не так, код ошибки: 404")

    def test_get_upcoming_contests(self):
        mock_data = [self.mock_response]
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.mock_contests

        with patch("requests.get") as mock_get:
            mock_get.return_value = mock_response
            from kontests import get_upcoming_contests

            current_time = datetime(2023, 6, 15, 12, 0, 0)
            expected_contests = [("Contest 1", "30-06-2023"), ("Contest 2", "30-06-2023")]
            contests = get_upcoming_contests(mock_data)
            mock_get.assert_called_once_with("https://kontests.net/api/v1/mock_site")
            self.assertEqual(contests, expected_contests)

    def test_parse_start_time_iso_format(self):
        from kontests import parse_start_time

        start_time = "2023-06-30T10:00:00+05:30"
        expected_time = datetime(2023, 6, 30, 10, 0, 0)
        parsed_time = parse_start_time(start_time)
        self.assertEqual(parsed_time, expected_time)

    def test_parse_start_time_yy_mm_dd_format(self):
        from kontests import parse_start_time

        start_time = "23-06-30"
        expected_time = datetime(2023, 6, 30, 0, 0, 0)
        parsed_time = parse_start_time(start_time)
        self.assertEqual(parsed_time, expected_time)


if __name__ == "__main__":
    unittest.main()
