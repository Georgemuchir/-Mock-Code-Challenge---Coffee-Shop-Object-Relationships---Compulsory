Coffee Shop Object Relationships Mock Code Challenge
This project is a mock code challenge for practicing object-oriented programming and relationships between classes in a coffee shop context. It is part of Phase 3 of the curriculum.

Features
Models key entities in a coffee shop, such as Customers, Orders, and Menu Items.
Demonstrates object relationships, including belongs_to and has_many relationships.
Provides methods for interacting with these models, such as creating orders, viewing order history, and managing menu items.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/coffee_shop_project.git
Navigate into the project directory:

bash
Copy code
cd coffee_shop_project
Install any required dependencies (if applicable).

Usage
Run the program:

bash
Copy code
python main.py
Follow the prompts to interact with the coffee shop's system.

Object Models
Customer
Represents a customer in the coffee shop.
Has a list of orders associated with them.
Order
Represents an order made by a customer.
Contains details like menu items ordered and the total price.
Menu Item
Represents an item available for purchase at the coffee shop.
Each order can consist of multiple menu items.
Relationships
A Customer has many Orders.
An Order belongs to a Customer and contains many Menu Items.
A Menu Item can be part of many Orders.