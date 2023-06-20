import unittest
import requests
from bs4 import BeautifulSoup

class TestPageCount(unittest.TestCase):
    def test_page_count(self):
        url = 'https://quotes.toscrape.com/page/1/'

        # Отправляем GET-запрос
        response = requests.get(url)

        # Создаем объект BeautifulSoup для парсинга HTML-кода страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим элемент с информацией о количестве страниц
        pagination = soup.find('ul', class_='pagination')
        last_page = pagination.find_all('a')[-2].text

        # Проверяем, что количество страниц соответствует ожидаемому значению
        self.assertEqual(int(last_page), 10)

if __name__ == '__main__':
    unittest.main()
