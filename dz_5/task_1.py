import requests
from bs4 import BeautifulSoup

def count_emojis(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    emoji_container = soup.find('ul', class_='emoji-list')
    emojis = emoji_container.find_all('li')

    return len(emojis)

nature_url = 'https://emojipedia.org/nature/'
music_url = 'https://emojipedia.org/music/'
science_url = 'https://emojipedia.org/science/'

nature_count = count_emojis(nature_url)
music_count = count_emojis(music_url)
science_count = count_emojis(science_url)

print(f"Количество эмодзи в разделе Nature: {nature_count}")
print(f"Количество эмодзи в разделе Music: {music_count}")
print(f"Количество эмодзи в разделе Science: {science_count}")
