import numpy as np

def solve_equation_system(matrix_file, solution_file):
    matrix = np.loadtxt(matrix_file, delimiter=' ')
    a = matrix[:, :-1]
    b = matrix[:, -1]

    try:
        inverse = np.linalg.inv(a)
        x = np.dot(inverse, b)
        np.savetxt(solution_file, x, fmt='%.1f')
        print('Система уравнений имеет решение')
    except np.linalg.LinAlgError:
        print('Система уравнений не имеет решения')

solve_equation_system('matrix.txt', 'solution.txt')
