from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Настройка драйвера
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Запуск в фоновом режиме (без графического интерфейса)
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие страницы
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url)

# Подождите немного, чтобы страница полностью загрузилась
time.sleep(5)

# Поиск элементов с ценами
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

# Сохранение цен в CSV файл
csv_file = 'prices.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовок
    for price in prices:
        writer.writerow([price.text])  # Запись текста цен

print(f"Цены сохранены в файл {csv_file}")

# Закрытие драйвера
driver.quit()
