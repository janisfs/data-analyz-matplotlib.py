from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Настройка драйвера
options = Options()
# options.add_argument('--headless')  # Запуск в фоновом режиме (без графического интерфейса)
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

# Инициализация драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Открытие страницы
url = 'https://www.divan.ru/category/divany-i-kresla'
driver.get(url)

# Ожидание загрузки элементов с ценами
try:
    prices = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.pY3d2 span"))
    )
except Exception as e:
    print(f"Ошибка при ожидании загрузки цен: {e}")
    driver.quit()
    exit()

# Сохранение цен в CSV файл
csv_file = 'price_divans.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовок
    for price in prices:  # Применение функции ко всем значениям в столбце 'Price'
        price_text = price.text.strip()
        if any(char.isdigit() for char in price_text):  # Проверка наличия цифр
            writer.writerow([price_text])


print(f"Цены сохранены в файл {csv_file}")

# Закрытие драйвера
driver.quit()
