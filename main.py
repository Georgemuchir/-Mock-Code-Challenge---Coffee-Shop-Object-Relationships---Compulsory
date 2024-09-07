from customer import Customer
from coffee import Coffee
from order import Order

# Global variable to store all orders
all_orders = []

# Create some customers
customer1 = Customer("Alice")
customer2 = Customer("Bob")

# Create some coffees
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# Create orders
order1 = customer1.create_order(coffee1, 5.0)
order2 = customer2.create_order(coffee1, 6.0)
order3 = customer1.create_order(coffee2, 7.0)

# Check customer orders
print("Alice's orders:")
for order in customer1.orders():
    print(f" - Coffee: {order.coffee.name}, Price: {order.price}")

print("Alice's coffees:")
for coffee in customer1.coffees():
    print(f" - {coffee.name}")

# Check coffee details
print("Espresso's orders:")
for order in coffee1.orders():
    print(f" - Customer: {order.customer.name}, Price: {order.price}")

print("Customers who ordered Espresso:")
for customer in coffee1.customers():
    print(f" - {customer.name}")

print("Number of Espresso orders:", coffee1.num_orders())
print("Average price of Espresso orders:", coffee1.average_price())
