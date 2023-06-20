import matplotlib.pyplot as plt
import random

# Список годов
years = [2010, 2011, 2012, 2013, 2014, 2015]

# Список стран
countries = ['Россия', 'США', 'Китай']

# Генерация случайных данных объемов торговли
data = {country: [random.randint(100, 300) for _ in range(len(years))] for country in countries}

# Построение графика
plt.figure(figsize=(10, 6))  # Размер графика

# Цикл по странам
for country in countries:
    plt.plot(years, data[country], label=country)  # Построение линий для каждой страны

# Настройки графика
plt.xlabel('Год')  # Подпись оси X
plt.ylabel('Объем торговли')  # Подпись оси Y
plt.title('Объемы торговли по странам')  # Заголовок графика
plt.legend()  # Легенда
plt.grid(True)  # Сетка

# Сохранение графика в файл
plt.savefig('trade_volume.png')

# Отображение графика
plt.show()
