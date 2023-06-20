import requests
from collections import Counter


def get_auth(data):
    values = data['entries']
    auth_list = [entry['Auth'] for entry in values]
    return auth_list


def count_auth(auth_list):
    count_auth_types = Counter(auth_list)
    return count_auth_types


def get_ratio_auth(count_auth_types, data):
    count = data['count']
    auth_ratio = []
    for key, value in count_auth_types.items():
        if key == '':
            ratio = value / count
            auth_ratio.append(f'Without Auth: {"{:.4f}".format(ratio)}')
        else:
            ratio = value / count
            auth_ratio.append(f'{key}: {"{:.4f}".format(ratio)}')
    return auth_ratio


def get_github_apis(data):
    values = data['entries']
    count = sum(1 for entry in values if entry['Link'].startswith('https://github.com/'))
    return count


def get_categories_and_auth(data):
    values = data['entries']
    categories = Counter(entry['Category'] for entry in values)
    return dict(categories)


if __name__ == "__main__":
    URL = "https://api.publicapis.org/entries"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        auth_list = get_auth(data=data)
        count_auth_types = count_auth(auth_list=auth_list)
        print("________________")
        print('Процентное соотношение разных видов Auth аутентификации к общему числу публичных API: ')
        ratio_auth = get_ratio_auth(count_auth_types=count_auth_types, data=data)
        print(ratio_auth)
        print("________________")
        print("Количество публичных API развернутых на github: ")
        github_apis = get_github_apis(data=data)
        print(github_apis)
        print("________________")
        print("Количество публичных API в определенных категориях: ")
        categories = get_categories_and_auth(data=data)
        print(categories)
    else:
        print(f'Ошибка, код ошибки: {response.status_code}')
