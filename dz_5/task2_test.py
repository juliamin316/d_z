import unittest
from unittest.mock import patch
from io import StringIO
import requests
from bs4 import BeautifulSoup

# Мок-класс для имитации ответа сервера на запрос
class MockResponse:
    def __init__(self, text):
        self.text = text

class TestEmojiCategories(unittest.TestCase):

    def setUp(self):
        self.url = 'https://emojipedia.org/'
        self.categories = ["nature", "music", "science"]

    @patch('sys.stdout', new_callable=StringIO)  # Перехватывает вывод на консоль
    @patch('requests.get')  # Перехватывает запросы get()
    def test_emoji_categories(self, mock_get, mock_stdout):
        mock_get.side_effect = [
            MockResponse('<div class="emoji-wrap"><a class="emoji">🌲</a><div class="annotation">Evergreen Tree</div></div>'),
            MockResponse('<div class="emoji-wrap"><a class="emoji">🎵</a><div class="annotation">Musical Note</div></div>'),
            MockResponse('<div class="emoji-wrap"><a class="emoji">🔬</a><div class="annotation">Microscope</div></div>')
        ]

        expected_output = [
            "Nature category:\n🌲: Evergreen Tree\n\n",
            "Music category:\n🎵: Musical Note\n\n",
            "Science category:\n🔬: Microscope\n\n"
        ]

        # Запуск кода, перехватывая вывод
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            import script  # Запускаем тестируемый код

            # Проверка вывода
            output = fake_stdout.getvalue()
            self.assertEqual(output, ''.join(expected_output))

        # Проверка вызовов функции requests.get()
        expected_calls = [
            unittest.mock.call('https://emojipedia.org/nature/'),
            unittest.mock.call('https://emojipedia.org/music/'),
            unittest.mock.call('https://emojipedia.org/science/')
        ]
        mock_get.assert_has_calls(expected_calls)

if __name__ == '__main__':
    unittest.main()
