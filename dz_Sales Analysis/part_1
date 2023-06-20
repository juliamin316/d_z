import requests
import numpy as np
import random

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
    count = 1
    country_dict = {}
    for country in unique_countries:
        if country not in country_dict:
            country_dict[country] = count
            count += 1
        regions.append(f"Region {country_dict[country]}")
    while len(regions) < data_len:
        regions.append(f"Region {count}")
        count += 1
    random.shuffle(regions)
    return regions
    
data_len = 5
city_names = ['Hawaii', 'Tokyo', 'Dusseldorf', 'Tokyo', 'Washington']
data = np.column_stack((generate_product_ids(data_len), generate_region_sales(data_len), generate_regions(data_len, city_names)))
