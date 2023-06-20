import unittest
import numpy as np
from solve_equation_system import solve_equation_system

class EquationSystemTest(unittest.TestCase):
    def test_solution_exists(self):
        # Создаем временный файл с матрицей, для тестирования
        matrix = np.array([[2, 3, 4],
                           [1, -1, 5],
                           [3, 2, 1]])
        np.savetxt('test_matrix.txt', matrix, fmt='%.1f')

        # Вызываем функцию для решения системы уравнений
        solve_equation_system('test_matrix.txt', 'test_solution.txt')

        # Загружаем полученное решение
        solution = np.loadtxt('test_solution.txt')

        # Проверяем, что система уравнений имеет решение
        self.assertTrue(np.allclose(np.dot(matrix[:, :-1], solution), matrix[:, -1]))

    def test_solution_not_exists(self):
        # Создаем временный файл с вырожденной матрицей, для тестирования
        matrix = np.array([[1, 2, 3],
                           [2, 4, 6],
                           [3, 6, 9]])
        np.savetxt('test_matrix.txt', matrix, fmt='%.1f')

        # Вызываем функцию для решения системы уравнений
        solve_equation_system('test_matrix.txt', 'test_solution.txt')

        # Проверяем, что система уравнений не имеет решения
        with self.assertRaises(FileNotFoundError):
            np.loadtxt('test_solution.txt')

if __name__ == '__main__':
    unittest.main()
