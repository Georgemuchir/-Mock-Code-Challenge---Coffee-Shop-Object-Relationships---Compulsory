class Coffee:
    def __init__(self, name):
        # Ensures the coffee name is a string with at least 3 characters
        if isinstance(name, str) and len(name) >= 3:
            self._name = name  # Assigns the name to the private attribute _name
        else:
            raise ValueError("Coffee name must be a string of at least 3 characters")

    # Getter method for the name property
    @property
    def name(self):
        return self._name  # Returns the private attribute _name

    # Method to return all orders for this coffee
    def orders(self):
        return [order for order in all_orders if order.coffee == self]

    # Method to return a unique list of all customers who ordered this coffee
    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    # Method to return the total number of orders for this coffee
    def num_orders(self):
        return len(self.orders())

    # Method to calculate and return the average price of orders for this coffee
    def average_price(self):
        orders = self.orders()
        if len(orders) == 0:
            return 0  # Returns 0 if there are no orders
        total_price = sum([order.price for order in orders])  # Sums the price of all orders
        return total_price / len(orders)  # Returns the average price
