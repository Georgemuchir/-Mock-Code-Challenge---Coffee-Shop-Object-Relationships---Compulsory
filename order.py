class Order:
    def __init__(self, customer, coffee, price):
        if isinstance(customer, Customer) and isinstance(coffee, Coffee):
            self._customer = customer
            self._coffee = coffee
            if isinstance(price, (int, float)) and 1.0 <= price <= 10.0:
                self._price = float(price)
            else:
                raise ValueError("Price must be a float between 1.0 and 10.0")
        else:
            raise ValueError("Invalid customer or coffee")
   
    @property
    def price(self):
        return self._price
   
    @property
    def customer(self):
        return self._customer
   
    @property
    def coffee(self):
        return self._coffee
