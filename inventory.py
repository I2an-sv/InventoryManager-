"""
 Role A (Lead)
"""


def calculate_stock_value(quantity, unit_price):
    """Calculates the total value of stock for a single product."""
    return quantity * unit_price


def calculate_discounted_price(price, discount_percent):
    """Calculates the final price of a product after a percentage discount."""
    return price - (price * discount_percent / 100)


if __name__ == "__main__":
    print(f"Stock value (qty=50, price=12.5): {calculate_stock_value(50, 12.5)}")
    print(f"Discounted price (price=200, discount=15%): {calculate_discounted_price(200, 15)}")