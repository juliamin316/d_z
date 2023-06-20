import requests
import numpy as np
import matplotlib.pyplot as plt

# Функция для загрузки списка стран
def load_country_names(n):
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    countries = [country['name']['common'] for country in response.json()[:n]]
    return countries

# Функция для генерации идентификаторов продуктов
def generate_product_ids(n):
    ids = np.random.randint(1, 1000, size=n)
    return ids

# Функция для генерации сумм продаж
def generate_sales(n):
    sales = np.random.randint(100, 1000, size=n)
    return sales

# Функция для генерации регионов продаж
def generate_sale_regions(n, country_names=[]):
    regions = np.random.choice(country_names, size=n, replace=True)
    return regions

# Загрузка списка стран
n = 50
country_names = load_country_names(n)[:6]

# Генерация данных
product_ids = generate_product_ids(n)
sales = generate_sales(n)
regions = generate_sale_regions(n, country_names)

# Сохранение данных в файл
data = np.column_stack((product_ids, sales, regions))
np.savetxt('sales_data.txt', data, delimiter=',', fmt='%s')

# Загрузка данных из файла
data = np.loadtxt('sales_data.txt', delimiter=',', dtype=str)

# Расчет общей суммы продаж
sales = data[:, 1].astype(int)
total_sales = np.sum(sales)
print("Общая сумма продаж для всех продуктов:", total_sales)

# Подсчет количества уникальных регионов продаж
regions = data[:, 2]
unique_regions = np.unique(regions)
num_unique_regions = unique_regions.size
print("Количество уникальных регионов продаж:", num_unique_regions)

# Расчет средней суммы продаж на продукт
average_sales_per_product = np.mean(sales)
print("Средняя сумма продаж на продукт:", average_sales_per_product)

# Определение продукта с наибольшей суммой продаж
max_sales_idx = np.argmax(sales)
product_id = data[max_sales_idx, 0]
print("Продукт с наибольшей суммой продаж имеет id:", product_id)

# Расчет суммы продаж для каждого региона продаж и построение круговой диаграммы
region_sales = {}
for region, sale in zip(regions, sales):
    region_sales[region] = region_sales.get(region, 0) + sale

labels = region_sales.keys()
values = region_sales.values()

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Сумма продаж по регионам')
plt.show()

# Определение топ 5 продуктов по продажам и построение круговой диаграммы
top_indices = np.argsort(sales)[-5:]
top_products = data[top_indices]
other_sales = np.sum(sales) - np.sum(sales[top_indices])

labels = np.append(top_products[:, 0], 'Other')
values = np.append(top_products[:, 1].astype(float), other_sales)

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Продажи по топ 5 продуктам')
plt.show()
