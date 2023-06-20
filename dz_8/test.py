import numpy as np

def test_create_zeros_array():
    zeros_arr = create_zeros_array(25)
    assert np.array_equal(zeros_arr, np.zeros(25)), "Test failed"

def test_create_ones_array():
    ones_arr = create_ones_array(10)
    assert np.array_equal(ones_arr, np.ones(10)), "Test failed"

def test_create_fives_array():
    fives_arr = create_fives_array(12)
    assert np.array_equal(fives_arr, np.full(12, 5)), "Test failed"

def test_create_range_array():
    arr1 = create_range_array(12, 52)
    assert np.array_equal(arr1, np.arange(12, 52)), "Test failed"

def test_create_even_range_array():
    arr2 = create_even_range_array(12, 52)
    assert np.array_equal(arr2, np.arange(12, 52, 2)), "Test failed"

def test_create_3x3_matrix():
    arr3 = create_3x3_matrix()
    assert np.array_equal(arr3, np.arange(1, 10).reshape(3, 3)), "Test failed"

def test_create_identity_matrix():
    arr4 = create_identity_matrix(5)
    assert np.array_equal(arr4, np.eye(5)), "Test failed"

def test_create_custom_matrix():
    arr5 = create_custom_matrix()
    assert np.array_equal(arr5, np.arange(0.01, 1.01, 0.01).reshape(10, 10)), "Test failed"

def test_create_number_matrix():
    arr6 = create_number_matrix()
    assert np.array_equal(arr6, np.arange(1, 26).reshape(5, 5)), "Test failed"

def test_extract_submatrix():
    arr6 = create_number_matrix()
    submatrix = extract_submatrix(arr6, 2, 5, 1, 5)
    expected_submatrix = np.array([[12, 13, 14, 15],
                                   [17, 18, 19, 20],
                                   [22, 23, 24, 25]])
    assert np.array_equal(submatrix, expected_submatrix), "Test failed"

def test_get_element():
    arr6 = create_number_matrix()
    element = get_element(arr6, 2, 4)
    assert element == 15, "Test failed"

def test_extract_column():
    arr6 = create_number_matrix()
    column = extract_column(arr6, 1)
    expected_column = np.array([2, 7, 12, 17, 22])
    assert np.array_equal(column, expected_column), "Test failed"

def test_extract_row():
    arr6 = create_number_matrix()
    row = extract_row(arr6, 4)
    expected_row = np.array([21, 22, 23, 24, 25])
    assert np.array_equal(row, expected_row), "Test failed"

def test_extract_rows():
    arr6 = create_number_matrix()
    rows = extract_rows(arr6, 3, 5)
    expected_rows = np.array([[16, 17, 18, 19, 20],
                              [21, 22, 23, 24, 25]])
    assert np.array_equal(rows, expected_rows), "Test failed"

def test_get_matrix_sum():
    arr6 = create_number_matrix()
    matrix_sum = get_matrix_sum(arr6)
    assert matrix_sum == 325, "Test failed"

def test_get_column_sums():
    arr6 = create_number_matrix()
    column_sums = get_column_sums(arr6)
    expected_column_sums = np.array([55, 60, 65, 70, 75])
    assert np.array_equal(column_sums, expected_column_sums), "Test failed"

# Запуск всех тестов
test_create_zeros_array()
test_create_ones_array()
test_create_fives_array()
test_create_range_array()
test_create_even_range_array()
test_create_3x3_matrix()
test_create_identity_matrix()
test_create_custom_matrix()
test_create_number_matrix()
test_extract_submatrix()
test_get_element()
test_extract_column()
test_extract_row()
test_extract_rows()
test_get_matrix_sum()
test_get_column_sums()
