import unittest
from city_function import get_city_country


class CitysCaseTest(unittest.TestCase):
    """Тесты для city_function"""

    def test_city_country(self):
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
