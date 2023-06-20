import pandas as pd
import datetime as dt

# Чтение данных из файла CSV
data = pd.read_csv('source_data.csv')

# Преобразование столбца 'date' в тип данных datetime
data['date'] = pd.to_datetime(data['date'])

# Фильтрация данных для января
data_january = data[data['date'].dt.month == 1]

# Добавление столбца 'day' с датой без времени
data['day'] = data['date'].dt.date

# Добавление столбца 'hour' с часом из времени
data['hour'] = data['date'].dt.hour

# Вывод первых нескольких строк данных
print(data.head())

# Фильтрация данных, где 'order_price' не равно 0
nonzero_orders = data.query('order_price != 0')

# Расчет процента заказов с нулевой ценой от общего числа заказов в январе
zero_price_percent = nonzero_orders.query('order_price == 0').shape[0] / data_january.shape[0] * 100

# Уникальные даты для заказов с нулевой ценой
zero_price_dates = data.query('order_price == 0')['day'].unique()

# Группировка по 'uid' и подсчет уникальных 'order_id'
top_users_by_order_count = data.groupby('uid')['order_id'].nunique().sort_values(ascending=False).head(100)

# Группировка по 'uid' и сумма 'order_price'
top_users_by_order_price = data.groupby('uid')['order_price'].sum().sort_values(ascending=False).head(100)

# Группировка по 'uid' и сумма 'cutlery'
top_users_by_cutlery = data.groupby('uid')['cutlery'].sum().sort_values(ascending=False).head(10)

# Группировка по 'uid' и сумма 'tips'
top_users_by_tips = data.groupby('uid')['tips'].sum().sort_values(ascending=False).head(20)

# Группировка по 'day' и сумма 'tips'
top_days_by_tips = data.groupby('day')['tips'].sum().sort_values(ascending=False).head(20)

# Подсчет количества значений в столбце 'cutlery'
cutlery_counts = data['cutlery'].value_counts()

# Подсчет количества уникальных значений в столбце 'uid'
unique_uid_count = data['uid'].nunique()

# Гистограмма распределения по часам
data['hour'].hist(bins=24)

# Группировка по 'uid' и сумма 'order_price' для топ-10 пользователей
top_10_users_by_order_price = data.groupby('uid')['order_price'].sum().sort_values(ascending=False).head(10)

# Фильтрация данных по дате и группировка по 'day', подсчет уникальных 'order_id' для топ-5 дат
top_5_days_by_order_count = data.loc[data['day'] != dt.date(2022, 1, 1)].groupby('day')['order_id'].nunique().sort_values(ascending=False).head(5)

