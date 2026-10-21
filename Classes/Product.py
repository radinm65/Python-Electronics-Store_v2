from abc import ABC
from Database.MySQLProgramQueries import MySQLProgramQueries


class Product(ABC):

    def __init__(self):
        self.id = None
        self.seller_id = None
        self.__date_created = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 3:
            raise ValueError(
                "Product name should be longer than 3 characters."
            )

        if len(new_name) > 100:
            raise ValueError(
                "Product name can't be longer than 100 characters."
            )
        self.__name = new_name

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):

        if len(new_brand) > 50:
            raise ValueError(
                "Brand can't be longer than 50 characters."
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
            new_price = int(new_price)
        except ValueError:
            raise ValueError(
                "Price must be a whole number."
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

    @date_created.setter
    def date_created(self, new_date_created):
        self.__date_created = new_date_created

    def save(self):
        extra_fields = self.extra_fields()
        return MySQLProgramQueries.add_product_query(self.seller_id,self.name, self.brand, self.price, self.category.lower(), *extra_fields.values())

    @staticmethod
    def get_approved_products():
        return MySQLProgramQueries.get_products_query("approved")
    
    @staticmethod
    def get_product_byID(product_id):
        return MySQLProgramQueries.get_product_byID_query(product_id)
    
    @staticmethod
    def edit_product(product_id, name, brand, price, field1, field2, field3):
        return MySQLProgramQueries.edit_product_query(product_id, name, brand, price, field1, field2, field3)
    
    
    @staticmethod
    def remove_product(product_id):
        return MySQLProgramQueries.delete_product_query(product_id) 
