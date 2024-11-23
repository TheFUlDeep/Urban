import numpy as np

# Создаем массив, заполненный единицами
arr = np.ones(5)
print("Исходный массив:", arr)

# Умножение на число
arr_mult = arr * 2
print("Массив, умноженный на 2:", arr_mult)

# Сложение с числом
arr_add = arr + 3
print("Массив с добавлением 3:", arr_add)





# Создаем массив с помощью arange
arr = np.arange(6, 11) # Создаем массив от 6 до 10 включительно
print("Исходный массив:", arr)

# Сумма всех элементов массива
sum_arr = np.sum(arr)
print("Сумма всех элементов массива:", sum_arr)

# Среднее значение элементов массива
mean_arr = np.mean(arr)
print("Среднее значение элементов массива:", mean_arr)

# Максимальное и минимальное значение в массиве
max_arr = np.max(arr)
min_arr = np.min(arr)
print("Максимальное значение в массиве:", max_arr)
print("Минимальное значение в массиве:", min_arr)





# Создаем двумерный массив (матрицу)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Исходная матрица:\n", matrix)

# Транспонирование матрицы
transposed_matrix = np.transpose(matrix)
print("Транспонированная матрица:\n", transposed_matrix)

# Умножение матрицы на число
matrix_mult = matrix * 3
print("Матрица, умноженная на 3:\n", matrix_mult)
