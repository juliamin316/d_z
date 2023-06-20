import requests
import numpy as np
import random
from bs4 import BeautifulSoup

def load_countries_name(data_len):
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    countries = [country['name']['common'] for country in response.json()[:data_len]]
    return countries
    
def generate_product_ids(data_len):
    return [random.randint(1, 25) for _ in range(data_len)]

def generate_region_sales(data_len):
    return [random.randint(100, 500) for _ in range(data_len)]
    
def generate_regions(data_len, country_names):
    regions = []
    unique_countries = list(set(country_names))
    for _ in range(data_len):
        if len(unique_countries) > 0:
            country = unique_countries.pop()
            regions.append(f"Region {country}")
        else:
            regions.append(f"Region {random.randint(1, 5)}")
    return regions

def extract_currency_codes():
    url = "https://www.exchangerate-api.com/docs/supported-currencies"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    currency_table = soup.find('table', class_='table-striped')
    rows = currency_table.find_all('tr')[1:]  # Exclude header row
    country_currency_code = {}
    for row in rows:
        cells = row.find_all('td')
        code = cells[0].text.strip()
        country = cells[2].text.strip()
        country_currency_code[country] = code
    return country_currency_code

def get_exchange_rate(currency_code):
    url = f"https://api.exchangerate-api.com/v4/latest/{currency_code}"
    response = requests.get(url)
    data = response.json()
    rates = data.get("rates")
    rub_value = rates.get("RUB")
    return rub_value

def convert_to_rub(data, currency_codes):
    converted_data = []
    for row in data:
        country = row[2]
        currency_code = currency_codes.get(country, "EUR")
        exchange_rate = get_exchange_rate(currency_code)
        sales = float(row[1])
        converted_sales = sales * exchange_rate
        converted_row = list(row) + [currency_code, converted_sales]
        converted_data.append(converted_row)
    return converted_data

data_len = 50
country_names = load_countries_name(data_len)
data = np.column_stack((generate_product_ids(data_len), generate_region_sales(data_len), country_names))

np.savetxt('data.txt', data, delimiter=',', fmt='%s') 
data = np.loadtxt('data.txt', delimiter=',', dtype=str)

currency_codes = extract_currency_codes()
converted_data = convert_to_rub(data, currency_codes)

np.savetxt('converted_data.txt', converted_data, delimiter=',', fmt='%s') 
