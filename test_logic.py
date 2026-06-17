import unittest
from inventory import calculate_stock_value, calculate_discounted_price


class TestInventory(unittest.TestCase):

    def test_stock_value(self):
        self.assertEqual(calculate_stock_value(50, 12.5), 625.0)

    def test_discounted_price(self):
        self.assertEqual(calculate_discounted_price(200, 15), 170.0)


if __name__ == "__main__":
    unittest.main()