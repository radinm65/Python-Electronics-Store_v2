from abc import ABC, abstractmethod
from datetime import datetime
from FileCommands import FileCommands
from IDGenerator import product_id_generator


class Product(ABC):

    def __init__(self):
        self.id = product_id_generator.next_id()
        self.seller_id = None
        self.__date_created = datetime.today()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 3:
            raise ValueError(
                "Product name should be longer than 3 characters."
            )
        self.__name = new_name

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        if len(new_brand) < 3:
            raise ValueError(
                "Brand should be longer than 3 characters."
            )

        if any(char.isdigit() for char in new_brand):
            raise ValueError(
                "Brand shouldn't have numbers."
            )
        self.__brand = new_brand

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        try:
            new_price = float(new_price)
        except ValueError:
            raise ValueError(
                "Price must be numeric."
            )

        if new_price <= 0:
            raise ValueError(
                "Price must be positive."
            )

        if new_price > 999999:
            raise ValueError(
                "Price can't be greater than 999999."
            )
        self.__price = new_price

    @property
    def date_created(self):
        return self.__date_created

    def save(self):
        new_product = {
            "id": self.id,
            "name": self.name,
            "brand": self.brand,
            "price": self.price,
            "category": self.category,
            "seller_id": self.seller_id,
            "date_created": self.date_created.isoformat(),
        }
        new_product.update(self.extra_fields())
        return FileCommands.add_data("./Database/UnapprovedProducts.json", new_product)

    @staticmethod
    def get_product_byID(product_id):
        from Classes.Phone import Phone
        from Classes.Laptop import Laptop
        from Classes.Camera import Camera

        product = Phone.get_product_byID(product_id)
        if product is None:
            product = Laptop.get_product_byID(product_id)
        if product is None:
            product = Camera.get_product_byID(product_id)
        return product
