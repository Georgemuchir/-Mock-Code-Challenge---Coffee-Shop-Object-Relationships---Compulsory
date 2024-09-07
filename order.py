class Order:
    def __init__(self, customer, coffee, price):
        # Ensures customer is an instance of Customer and coffee is an instance of Coffee
        if isinstance(customer, Customer) and isinstance(coffee, Coffee):
            self._customer = customer  # Assigns the customer to the private attribute _customer
            self._coffee = coffee      # Assigns the coffee to the private attribute _coffee

            # Validates price to ensure it's a float between 1.0 and 10.0
            if isinstance(price, (int, float)) and 1.0 <= price <= 10.0:
                self._price = float(price)  # Converts the price to float and assigns it to _price
            else:
                raise ValueError("Price must be a number between 1.0 and 10.0")
        else:
            raise ValueError("Invalid customer or coffee")

    # Getter method for the price property
    @property
    def price(self):
        return self._price  # Returns the private attribute _price

    # Getter method for the customer property
    @property
    def customer(self):
        return self._customer  # Returns the private attribute _customer

    # Getter method for the coffee property
    @property
    def coffee(self):
        return self._coffee  # Returns the private attribute _coffee
