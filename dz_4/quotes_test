import unittest
from your_module import scrape_quotes

class TestScrapeQuotes(unittest.TestCase):
    def test_scrape_quotes(self):
        quotes, num_pages = scrape_quotes()

        self.assertTrue(quotes)  # Проверяем, что список цитат не пустой
        self.assertGreater(num_pages, 0)  # Проверяем, что количество страниц больше 0
        self.assertEqual(len(quotes), num_pages * 10)  # Проверяем, что количество цитат равно ожидаемому

if __name__ == '__main__':
    unittest.main()
