import requests
from bs4 import BeautifulSoup

url = 'https://emojipedia.org/'

categories = ["nature", "music", "science"]

for category in categories:
    category_url = url + category + '/'
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    emoji_divs = soup.find_all('div', class_='emoji-wrap')

    print(f"{category.capitalize()} category:")
    for emoji_div in emoji_divs:
        emoji_name = emoji_div.find('a', class_='emoji').text.strip()
        emoji_description = emoji_div.find('div', class_='annotation').text.strip()
        print(f"{emoji_name}: {emoji_description}")
    print()
