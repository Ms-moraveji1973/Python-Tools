def check_inventory(func):
    def wrapper(product, quantity, *args, **kwargs):
        inventory = {"item1": 10, "item2": 5, "item3": 8}
        if product in inventory and inventory[product] >= quantity:
            print(f"Order is feasible. {quantity} units of {product} have been added to the shopping cart.")
            return func(product, quantity, *args, **kwargs)
        else:
            print(f"Unfortunately, the product {product} with a quantity of {quantity} is not available in the inventory.")
    return wrapper

# Define a decorator for calculating order price
def calculate_price(func):
    def wrapper(product, quantity, *args, **kwargs):
        prices = {"item1": 20, "item2": 30, "item3": 15}
        total_price = func(product, quantity, *args, **kwargs)
        unit_price = prices.get(product, 0)
        print(f"Unit price of {product}: ${unit_price}")
        print(f"Total order price: ${total_price}")
        return total_price
    return wrapper

# Define the order function
@check_inventory
@calculate_price
def place_order(product, quantity):
    print(f"Order for {quantity} units of {product} has been placed.")
    return quantity * prices.get(product, 0)  # There is an error here, as 'prices' is not available until the definition of the 'calculate_price' function.

# Test the functionality of decorators
place_order("item1", 2)
