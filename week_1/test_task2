import unittest

class TestTextFormatting(unittest.TestCase):
    def test_text_formatting(self):
        # Подготовка тестовых данных
        input_file = 'test_input.txt'
        output_file = 'test_output.txt'
        expected_output = "KP2.2-123 - Text 1\nKP2.2-456 - Text 2\n"

        # Запись тестовых данных во входной файл
        test_data = "ID1 KP2.2-123 - Text 1\nID2 KP2.2-456 - Text 2"
        write_data(input_file, test_data)

        # Выполнение кода, который будет протестирован
        write_data(output_file, format_text(read_data(input_file)))

        # Чтение выходного файла и сравнение с ожидаемым результатом
        with open(output_file) as file:
            output_data = file.read()

        self.assertEqual(output_data, expected_output)

        # Очистка тестовых файлов
        remove_files(input_file, output_file)

if __name__ == '__main__':
    unittest.main()
