import pandas as pd
import matplotlib.pyplot as plt

# Шаг 1: Чтение данных из очищенного CSV файла
df = pd.read_csv('cleaned_prices.csv')

# Шаг 2: Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=20, color='blue', edgecolor='black')

# Шаг 3: Настройка графика
plt.title('Гистограмма цен на квартиры')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество предложений')
plt.grid(True)

# Шаг 4: Отображение гистограммы
plt.show()
