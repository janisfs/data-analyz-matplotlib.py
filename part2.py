from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка драйвера
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Запуск в фоновом режиме (без графического интерфейса)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Инициализация драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Открытие страницы
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url)

# Подождите немного, чтобы страница полностью загрузилась
time.sleep(5)

# Поиск элементов с ценами
price_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "c6e8ba9eec--price--2nM5Y")]')

# Извлечение и вывод цен
prices = [price.text for price in price_elements]
for price in prices:
    print(price)

# Закрытие драйвера
driver.quit()