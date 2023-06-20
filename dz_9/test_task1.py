import numpy as np
import os

# Генерация входных данных
input_matrix = np.array([[1, 2, 3, 4],
                         [5, 6, 7, 8],
                         [9, 10, 11, 12]])

# Сохранение входной матрицы в файл
np.savetxt('matrix.txt', input_matrix, fmt='%d')

# Тест функции load_matrix_from_file
loaded_matrix = load_matrix_from_file('matrix.txt')

# Проверка загруженной матрицы
assert np.array_equal(input_matrix, loaded_matrix), "Ошибка: загруженная матрица отличается от входной"

# Тест функции solve_linear_system
solution = solve_linear_system(input_matrix)

# Проверка решения
expected_solution = np.array([-1.00000000e+00, 2.00000000e+00, -1.00000000e+00])
assert np.allclose(solution, expected_solution), "Ошибка: неправильное решение линейной системы"

# Тест функции save_solution_to_file
save_solution_to_file('solution.txt', solution)

# Проверка сохраненного решения
saved_solution = np.loadtxt('solution.txt')
assert np.allclose(solution, saved_solution), "Ошибка: сохраненное решение отличается от ожидаемого"

# Удаление временных файлов
os.remove('matrix.txt')
os.remove('solution.txt')

print("Все тесты пройдены успешно.")
