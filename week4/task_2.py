import requests


def get_value_and_currency(input_data):
    data = input_data.split()
    value, currency = data[0], data[1]
    return value, currency


def request(convert_currency):
    currency = convert_currency
    URL = f'https://open.er-api.com/v6/latest/{currency}'
    response = requests.get(URL)
    return response.json()


def find_price(data, local_currency, convert_currency):
    rates = data['rates']
    price = rates.get(local_currency)
    return price


def convert(value, price, local_currency, convert_currency):
    value = float(value)
    result = value / price
    return f'Ваши {value} {local_currency} это {"{:.2f}".format(result)} {convert_currency}'


if __name__ == "__main__":
    input_data = input("Введите число и валюту в виде 100 RUB, 1000 USD  : ")
    convert_currency = input("Введите в какую валюту хотите преобразовать: ")
    value, local_currency = get_value_and_currency(input_data)
    data_json = request(convert_currency)
    price = find_price(data_json, local_currency, convert_currency)
    result = convert(value, price, local_currency, convert_currency)
    print(result)
