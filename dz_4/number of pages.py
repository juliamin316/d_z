import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/page/1/'

# Отправляем GET-запрос
response = requests.get(url)

# Создаем объект BeautifulSoup для парсинга HTML-кода страницы
soup = BeautifulSoup(response.text, 'html.parser')

# Находим элемент с информацией о количестве страниц
pagination = soup.find('ul', class_='pagination')
last_page = pagination.find_all('a')[-2].text

print(f"Количество страниц: {last_page}")

# Количество страниц: 10
