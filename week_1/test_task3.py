class TestFormatText(unittest.TestCase):
    def test_format_text(self):
        input_file = 'input.txt'
        output_file = 'output.txt'
        expected_output = 'She married a very \nnice young architect \nfrom Belfast, whom \nshe met on a bus.\n'
        symbols_q = 21

        # Чтение входных данных из файла
        input_data = read_data(input_file)

        # Форматирование текста
        formatted_text = format_text(input_data, symbols_q)

        # Запись отформатированного текста в файл
        write_data(output_file, formatted_text)

        # Проверка совпадения с ожидаемым результатом
        with open(output_file) as f:
            actual_output = f.read()

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
