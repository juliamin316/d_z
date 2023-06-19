import requests


def get_joke_types(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [joke['type'] for joke in data]
    else:
        print(f"Error: {response.status_code}")
        return []


if __name__ == "__main__":
    url = 'https://official-joke-api.appspot.com/jokes/ten'
    joke_types = get_joke_types(url)
    print(joke_types)

