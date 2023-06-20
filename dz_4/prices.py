import requests
from bs4 import BeautifulSoup

def scrape_catalog(url):
    # Отправляем GET-запрос на первую страницу каталога
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []

    # Ищем все элементы товаров на странице
    product_elements = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for product_element in product_elements:
        # Извлекаем наименование и цену товара
        name = product_element.find('h4', class_='card-title').text.strip()
        price = product_element.find('h5').text.strip()

        # Добавляем товар в список
        products.append({'name': name, 'price': price})

    # Проверяем наличие следующей страницы каталога
    next_page = soup.find('a', class_='next page-link')
    if next_page:
        # Если следующая страница существует, рекурсивно вызываем функцию для нее
        next_page_url = next_page['href']
        products += scrape_catalog(next_page_url)

    return products

if __name__ == '__main__':
    url = 'https://scrapingclub.com/exercise/list_basic/'
    catalog = scrape_catalog(url)

    # Выводим список товаров
    for product in catalog:
        print(f"Наименование: {product['name']}, Цена: {product['price']}")
