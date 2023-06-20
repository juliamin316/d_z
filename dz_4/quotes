import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = 'https://quotes.toscrape.com/page/1/'
    quotes = []
    page = 1

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        quote_elements = soup.find_all('div', class_='quote')
        for quote_element in quote_elements:
            text = quote_element.find('span', class_='text').text.strip()
            author = quote_element.find('small', class_='author').text.strip()
            quotes.append(f'{text} - (c) {author}')

        next_button = soup.find('li', class_='next')
        if next_button is None:
            break

        page += 1
        url = f'https://quotes.toscrape.com/page/{page}/'

    return quotes, page

quotes, num_pages = scrape_quotes()

for idx, quote in enumerate(quotes):
    print(f'{idx+1}. {quote}')

print(f'На сайте {num_pages} страниц и {len(quotes)} цитат')
