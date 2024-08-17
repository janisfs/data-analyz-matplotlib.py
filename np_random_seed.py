import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
np.random.seed(0)  # для воспроизводимости результатов
x = np.random.rand(50)  # массив из 50 случайных чисел
y = np.random.rand(50)  # массив из 50 случайных чисел

# Построение диаграммы рассеяния
plt.scatter(x, y)

# Установка заголовка и меток осей
plt.title('Диаграмма рассеяния')
plt.xlabel('X')
plt.ylabel('Y')

# Отображение диаграммы рассеяния
plt.show()