import unittest
from inventory import calculate_stock_value, calculate_discounted_price, calculate_profit_margin

class TestInventory(unittest.TestCase):

    def test_stock_value(self):
        self.assertEqual(calculate_stock_value(50, 12.5), 625.0)

    def test_discounted_price(self):
        self.assertEqual(calculate_discounted_price(200, 15), 170.0)

    def test_profit_margin(self):
        self.assertEqual(calculate_profit_margin(100, 150), 50.0)

if __name__ == "__main__":
    unittest.main()
