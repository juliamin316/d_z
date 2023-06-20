import numpy as np

def load_matrix_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        matrix = [[float(num) for num in line.split()] for line in lines]
    return np.array(matrix)

def save_solution_to_file(filename, solution):
    np.savetxt(filename, solution, fmt='%.1f')

def solve_linear_system(matrix):
    a = matrix[:, :-1]
    b = matrix[:, -1]
    return np.linalg.solve(a, b)

# Загрузка матрицы из файла
matrix = load_matrix_from_file('matrix.txt')

# Решение линейной системы
solution = solve_linear_system(matrix)

# Сохранение решения в файл
save_solution_to_file('solution.txt', solution)
