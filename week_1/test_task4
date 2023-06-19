import unittest

class TestFormatText(unittest.TestCase):
    def test_format_text(self):
        input_file = 'input.txt'
        output_file = 'output.txt'
        expected_output = 'word1,3\nword2,2\nword3,2\nword4,1\nword5,1\nword6,1\nword7,1\nword8,1\nword9,1\nword10,1\n'

        # Чтение входных данных из файла
        input_data = read_data(input_file)

        # Форматирование текста
        formatted_text = format_text(input_data)

        # Запись отформатированного текста в файл
        write_data(output_file, formatted_text)

        # Проверка совпадения с ожидаемым результатом
        with open(output_file) as f:
            actual_output = f.read()

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
