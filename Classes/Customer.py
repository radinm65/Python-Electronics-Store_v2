from Classes.User import User
from Database.MySQLProgramQueries import MySQLProgramQueries
from datetime import datetime


class Customer(User):
    def __init__(self):
        super().__init__()
        self.id = None

    def save(self):
        return MySQLProgramQueries.add_customer_query(
            self.firstname,
            self.lastname,
            self.username,
            self.password,
            self.age,
            self.phone_num,
            self.address,
            self.balance,
        )


    def add_to_cart(self, product_id):
        return MySQLProgramQueries.add_cart_item_query(self.id, product_id)


    def add_to_favorites(self, product_id):
        return MySQLProgramQueries.add_customer_favorites_query(self.id, product_id)


    def remove_from_favorites(self, product_id):
        return MySQLProgramQueries.delete_customer_favorite_query(self.id, product_id)


    def remove_from_cart(self, product_id):
        return MySQLProgramQueries.delete_cart_item_query(self.id, product_id)


    def checkout(self):
        customer_cart_items = MySQLProgramQueries.get_customer_cart_items_query(self.id)

        if len(customer_cart_items) == 0:
            raise ValueError("Cart is empty.")

        total_price = MySQLProgramQueries.get_customer_cart_total_price_query(self.id)

        if total_price > self.balance:
            raise ValueError("Not enough balance.")

        customer_cart_items_tuple = [
            (item["customer_id"], item["product_id"]) for item in customer_cart_items
        ]

        MySQLProgramQueries.add_cart_items_to_sales_query(customer_cart_items_tuple)

        MySQLProgramQueries.add_cart_total_to_sellers_balance_query(self.id)
        
        customer_balance = MySQLProgramQueries.get_customer_balance_query()
        
        customer_balance_set_amount = customer_balance - total_price
        
        MySQLProgramQueries.set_customer_balance_query(customer_balance_set_amount, self.id)
        
        MySQLProgramQueries.delete_all_customer_cart_items_query(self.id)



    def add_favorites_to_cart(self):
        customer_favorites = MySQLProgramQueries.get_customer_favorites_query(self.id)
        
        if len(customer_favorites) == 0:
            raise ValueError("Favorites is empty.")
        
        MySQLProgramQueries.delete_all_customer_favorites_query(self.id)
        
        return MySQLProgramQueries.add_many_cart_item_query(customer_favorites)


    def change_balance(self, new_balance):
        return MySQLProgramQueries.set_customer_balance_query(new_balance, self.id)
        

    @staticmethod
    def from_dict(data):
        customer = Customer()
        customer.id = data["id"]
        customer.firstname = data["firstname"]
        customer.lastname = data["lastname"]
        customer.username = data["username"]
        customer.set_hashed_password(data["password"])
        customer.age = str(data["age"])
        customer.phone_num = data["phone_num"]
        customer.address = data["address"]
        customer.balance = data["balance"]
        return customer

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Firstname: {self.firstname}\n"
            f"Lastname: {self.lastname}\n"
            f"Username: {self.username}\n"
            f"Age: {self.age}\n"
            f"Phone_num: {self.phone_num}\n"
            f"Address: {self.address}\n"
            f"Balance: {self.balance}\n"
        )
