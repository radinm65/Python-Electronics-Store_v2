from Classes.User import User
from Classes.Product import Product
from Classes.CustomerEmployee import CustomerEmployee
from IDGenerator import customer_id_generator
from FileCommands import FileCommands
from datetime import datetime


class Customer(User):
    def __init__(self):
        super().__init__()
        self.id = customer_id_generator.next_id()
        self.cart = None
        self.favorites = None
        self.bought = None

    def save(self):
        new_customer = {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "password": self.password,
            "age": self.age,
            "phone_num": self.phone_num,
            "address": self.address,
            "balance": self.balance,
            "cart": self.cart,
            "favorites": self.favorites,
            "bought": self.bought,
        }
        return FileCommands.add_data("./Database/Customers.json", new_customer)



    def add_to_cart(self, product_id):
        product = Product.get_product_byID(product_id)

        if product is None:
            raise ValueError("Product not found.")

        customers = CustomerEmployee.get_customers()

        for customer in customers:
            if customer["id"] == self.id:

                if product_id in customer["cart"]:
                    raise ValueError("Already in cart.")

                customer["cart"].append(product_id)
                return FileCommands.save_file_data(
                    "./Database/Customers.json", customers
                )
        return False

    def add_to_favorites(self, product_id):

        product = Product.get_product_byID(product_id)

        if product is None:
            raise ValueError("Product not found.")

        customers = CustomerEmployee.get_customers()
        for customer in customers:
            if customer["id"] == self.id:

                if product_id in customer["favorites"]:
                    raise ValueError("Already in favorites.")

                customer["favorites"].append(product_id)
                return FileCommands.save_file_data(
                    "./Database/Customers.json", customers
                )
        return False

    def remove_from_favorites(self, product_id):
        customers = CustomerEmployee.get_customers()

        for customer in customers:
            if customer["id"] == self.id:

                if product_id not in customer["favorites"]:
                    raise ValueError("Product is not in favorites.")

                customer["favorites"].remove(product_id)
                return FileCommands.save_file_data(
                    "./Database/Customers.json", customers
                )
        return False

    def remove_from_cart(self, product_id):
        customers = CustomerEmployee.get_customers()

        for customer in customers:
            if customer["id"] == self.id:

                if product_id not in customer["cart"]:
                    raise ValueError("Product is not in cart.")

                customer["cart"].remove(product_id)
                return FileCommands.save_file_data(
                    "./Database/Customers.json", customers
                )
        return False

    def checkout(self):
        customers = CustomerEmployee.get_customers()
        for customer in customers:
            if customer["id"] == self.id:
                if len(customer["cart"]) == 0:
                    raise ValueError("Cart is empty.")
                sellers = FileCommands.get_file_data("./Database/Sellers.json")
                purchase_date = datetime.today().isoformat()
                total_price = 0
                
                for product_id in customer["cart"]:
                    product = Product.get_product_byID(product_id)
                    if product is None:
                        continue
                    total_price += product["price"]
                if total_price > customer["balance"]:
                    raise ValueError("Not enough balance.")
                # خرید انجام شود
                for product_id in customer["cart"]:
                    product = Product.get_product_byID(product_id)
                    if product is None:
                        continue
                    customer["bought"].append(
                        {"product_id": product_id, "date": purchase_date}
                    )
                    # پیدا کردن فروشنده
                    for seller in sellers:
                        if seller["id"] == product["seller_id"]:
                            seller["balance"] += product["price"]
                            seller["sold"].append(
                                {"product_id": product_id, "date": purchase_date}
                            )
                            break
                customer["balance"] -= total_price
                # خالی کردن سبد
                customer["cart"].clear()
                FileCommands.save_file_data("./Database/Sellers.json", sellers)
                return FileCommands.save_file_data(
                    "./Database/Customers.json", customers
                )
        return False


    @staticmethod
    def add_cart_to_favorites(customer_id):

        customers = CustomerEmployee.get_customers()

        for customer in customers:

            if customer["id"] == customer_id:

                if len(customer["favorites"]) == 0:
                    raise ValueError("Favorites is empty.")

                for product_id in customer["favorites"]:

                    if product_id not in customer["cart"]:
                        customer["cart"].append(product_id)

                customer["favorites"] = []

                return FileCommands.save_file_data(
                    "./Database/Customers.json",
                    customers
                )

        return False

    @staticmethod
    def add_to_balance(customer_id, new_balance):

        customers = CustomerEmployee.get_customers()

        for customer in customers:

            if customer["id"] == customer_id:

                customer["balance"] = new_balance

                return FileCommands.save_file_data(
                    "./Database/Customers.json",
                    customers
                )

        return False

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
        customer.cart = data["cart"]
        customer.favorites = data["favorites"]
        customer.bought = data["bought"]

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
            f"Cart: {self.cart}\n"
            f"Favorites: {self.favorites}\n"
            f"Bought: {self.bought}\n"
        )
