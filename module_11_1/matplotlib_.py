import matplotlib.pyplot as plt
import random

# Данные для построения графика
x = [i for i in range(0, 11)]
y = [i**2 for i in x]

# Построение графика
plt.plot(x, y)
plt.title('Простая линейная диаграмма')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()





# Данные для построения гистограммы
data = [random.gauss(0, 1) for _ in range(1000)]

# Построение гистограммы
plt.hist(data, bins=30, edgecolor='black')
plt.title('Гистограмма')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.show()




# Данные для построения точечной диаграммы
x = [random.uniform(-1, 1) for _ in range(100)]
y = [random.uniform(-1, 1) for _ in range(100)]

# Построение точечной диаграммы
plt.scatter(x, y)
plt.title('Точечная диаграмма')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
