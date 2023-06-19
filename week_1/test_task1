import unittest

class TestDataFormatting(unittest.TestCase):
    def test_data_formatting(self):
        # Подготовка тестовых данных
        input_file = 'test_data.txt'
        output_file = 'test_output.csv'
        expected_output = "name,grade\nAlice Smith,90\nBob Johnson,85\n"

        # Запись тестовых данных во входной файл
        test_data = "ID1 KP2.2-Alice: 90\nID2 KP2.2-Bob: 85"
        write_data(input_file, test_data)

        # Выполнение кода, который будет протестирован
        write_data(output_file, format_data(read_data(input_file)))

        # Чтение выходного файла и сравнение с ожидаемым результатом
        with open(output_file) as file:
            output_data = file.read()

        self.assertEqual(output_data, expected_output)

        # Очистка тестовых файлов
        remove_files(input_file, output_file)

if __name__ == '__main__':
    unittest.main()

