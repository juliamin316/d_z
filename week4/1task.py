import requests 
def get_type(response):
    t_list = []
    data = response.json()
    for i in data:
        type = i['type']
        t_list.append(type)
    return t_list

if __name__ == "__main__":
    URL = 'https://official-joke-api.appspot.com/jokes/ten'
    response = requests.get(URL)
    if response.status_code == 200:
        print(response.status_code)
        print("Запрос выполнен успешно")
        print(get_type(response=response))
    else:
        print(response.status_code)
        print('Ошибка')
        
