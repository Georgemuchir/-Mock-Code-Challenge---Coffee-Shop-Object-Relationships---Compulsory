class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Coffee name must be a string of at least 3 characters")
   
    @property
    def name(self):
        return self._name
   
    def orders(self):
        return [order for order in all_orders if order.coffee == self]
   
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
   
    def num_orders(self):
        return len(self.orders())
   
    def average_price(self):
        orders = self.orders()
        if len(orders) == 0:
            return 0
        total_price = sum([order.price for order in orders])
        return total_price / len(orders)
