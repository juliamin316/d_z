import numpy as np

def create_zeros_array(size):
    return np.zeros(size)

def create_ones_array(size):
    return np.ones(size)

def create_fives_array(size):
    return np.full(size, 5)

def create_range_array(start, end):
    return np.arange(start, end)

def create_even_range_array(start, end):
    return np.arange(start, end, 2)

def create_3x3_matrix():
    return np.arange(1, 10).reshape(3, 3)

def create_identity_matrix(size):
    return np.eye(size)

def create_custom_matrix():
    return np.arange(0.01, 1.01, 0.01).reshape(10, 10)

def create_number_matrix():
    return np.arange(1, 26).reshape(5, 5)

def extract_submatrix(matrix, row_start, row_end, col_start, col_end):
    return matrix[row_start:row_end, col_start:col_end]

def get_element(matrix, row_index, col_index):
    return matrix[row_index, col_index]

def extract_column(matrix, col_index):
    return matrix[:, col_index]

def extract_row(matrix, row_index):
    return matrix[row_index, :]

def extract_rows(matrix, row_start, row_end):
    return matrix[row_start:row_end, :]

def get_matrix_sum(matrix):
    return np.sum(matrix)

def get_column_sums(matrix):
    return np.sum(matrix, axis=0)

# Пример использования
zeros_arr = create_zeros_array(25)
print(zeros_arr)

ones_arr = create_ones_array(10)
print(ones_arr)

fives_arr = create_fives_array(12)
print(fives_arr)

arr1 = create_range_array(12, 52)
print(arr1)

arr2 = create_even_range_array(12, 52)
print(arr2)

arr3 = create_3x3_matrix()
print(arr3)

arr4 = create_identity_matrix(5)
print(arr4)

arr5 = create_custom_matrix()
print(arr5)

arr6 = create_number_matrix()
print(arr6)

submatrix = extract_submatrix(arr6, 2, 5, 1, 5)
print(submatrix)

element = get_element(arr6, 2, 4)
print(element)

sub_arr = extract_column(arr6, 1)
print(sub_arr)

row = extract_row(arr6, 4)
print(row)

rows = extract_rows(arr6, 3, 5)
print(rows)

matrix_sum = get_matrix_sum(arr6)
print(matrix_sum)

column_sums = get_column_sums(arr6)
print(column_sums)
