import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv('prices.csv')

# Функция для удаления символов "₽/мес." и преобразования строки в числовое значение
def clean_price(price):
    if isinstance(price, str):
        return int(price.replace('₽/мес.', '').replace(' ', ''))
    return price

# Применение функции ко всем значениям в столбце 'Price'
df['Price'] = df['Price'].apply(clean_price)

# Проверка результата
print(df.head())

# Сохранение обновленного DataFrame в новый CSV файл
df.to_csv('cleaned_prices.csv', index=False)
