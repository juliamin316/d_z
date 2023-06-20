import unittest
from scraper import scrape_catalog

class CatalogScrapingTest(unittest.TestCase):
    def test_scrape_catalog(self):
        url = 'https://scrapingclub.com/exercise/list_basic/'
        catalog = scrape_catalog(url)

        # Проверяем, что список товаров не пустой
        self.assertGreater(len(catalog), 0)

        # Проверяем, что каждый товар имеет наименование и цену
        for product in catalog:
            self.assertIn('name', product)
            self.assertIn('price', product)

if __name__ == '__main__':
    unittest.main()
