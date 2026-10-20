from Classes.Employee import Employee
from Classes.Ticket import Ticket
from Database.MySQLProgramQueries import MySQLProgramQueries

class CustomerEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.id = None


    @staticmethod
    def get_customers():
        return MySQLProgramQueries.get_customers_query()

    @staticmethod
    def get_customer_byID(customer_id):
        return MySQLProgramQueries.get_customer_byID_query(customer_id)


    @staticmethod
    def delete_customer(customer_id):
        return MySQLProgramQueries.delete_customer_query(customer_id)


    @classmethod
    def from_dict(cls, data):
        customer_employee = cls()
        customer_employee.id = data["id"]
        customer_employee.firstname = data["firstname"]
        customer_employee.lastname = data["lastname"]
        customer_employee.username = data["username"]
        customer_employee.set_hashed_password(data["password"])
        customer_employee.age = str(data["age"])
        customer_employee.phone_num = data["phone_num"]
        customer_employee.address = data["address"]
        customer_employee.bank_account_num = data["bank_account_num"]
        customer_employee.salary = data["salary"]
        customer_employee.date_hired = data["date_hired"]

        return customer_employee


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
