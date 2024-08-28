import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV файла
df = pd.read_csv('price_divans.csv')

# Построение гистограммы
plt.figure(figsize=(10, 6))  # Размер графика
plt.hist(df['Price'], bins=30, edgecolor='black')  # Количество интервалов
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.grid(True)

# Отображение графика
plt.show()

