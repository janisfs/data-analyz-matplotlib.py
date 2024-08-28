import numpy as np
import matplotlib.pyplot as plt


# a = np.array([1, 2, 3, 4])
# print(a)

# a = np.zeros((3, 3)) # создание массива из нулей

# a = np.ones((2, 5)) # создание массива из единиц

# a = np.random.random((2, 5)) # создание массива из случайных чисел в диапазоне от 0 до 1

# a = np.arange(0, 10, 2) # создание массива от 0 до 10 с шагом 2


x = np.linspace(-10, 10, 100)  # создание массива из 100 случайных чисел в диапазоне от -10 до 10
y = x**2  # создание массива из случайных чисел в диапазоне от -10 до 10

# Построение графика
plt.title("График y = x**2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.plot(x, y)
plt.show()