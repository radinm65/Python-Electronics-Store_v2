from Classes.Employee import Employee
from Classes.Ticket import Ticket
from Classes.Product import Product
from Classes.Phone import Phone
from Classes.Laptop import Laptop
from Classes.Camera import Camera
from Database.MySQLProgramQueries import MySQLProgramQueries


class SellerEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.id = None

    @staticmethod
    def get_unapproved_sellers():
        return MySQLProgramQueries.get_sellers_query("pending")

    @staticmethod
    def get_unapproved_products():
        return MySQLProgramQueries.get_products_query("pending")

    @staticmethod
    def approve_seller(seller_id):
        return MySQLProgramQueries.approve_seller_query(seller_id)

    @staticmethod
    def approve_product(product_id):
        return MySQLProgramQueries.approve_product_query(product_id)

    # @staticmethod
    # def check_unapproved_sellerID(sellerID):
    #     unapproved_sellers = SellerEmployee.get_unapproved_sellers()
    #     for us in unapproved_sellers:
    #         if sellerID == us["id"]:
    #             return True
    #     return False

    @staticmethod
    def remove_seller(seller_id):
        return MySQLProgramQueries.delete_seller_query(seller_id)

    @staticmethod
    def remove_product(product_id):
        return MySQLProgramQueries.delete_product_query(product_id)

    @staticmethod
    def get_sellers():
        return MySQLProgramQueries.get_sellers_query("approved")

    @staticmethod
    def get_seller_byID(seller_id):
        return MySQLProgramQueries.get_approved_seller_query(seller_id)

    @classmethod
    def from_dict(cls, data):
        seller_employee = cls()
        seller_employee.id = data["id"]
        seller_employee.firstname = data["firstname"]
        seller_employee.lastname = data["lastname"]
        seller_employee.username = data["username"]
        seller_employee.set_hashed_password(data["password"])
        seller_employee.age = str(data["age"])
        seller_employee.phone_num = data["phone_num"]
        seller_employee.address = data["address"]
        seller_employee.bank_account_num = data["bank_account_num"]
        seller_employee.salary = data["salary"]
        seller_employee.date_hired = data["date_hired"]

        return seller_employee

    def __str__(self):
        return (
            f"Firstname: {self.firstname}\n"
            f"Lastname: {self.lastname}\n"
            f"Username: {self.username}\n"
            f"Age: {self.age}\n"
            f"Phone_num: {self.phone_num}\n"
            f"Address: {self.address}\n"
            f"Bank_account_num: {self.bank_account_num}\n"
            f"Salary: {self.salary}\n"
            f"Date_hired: {self.date_hired}\n"
        )
