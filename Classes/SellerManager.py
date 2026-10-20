from Classes.Manager import Manager
from Database.MySQLProgramQueries import MySQLProgramQueries


class SellerManager(Manager):
    def __init__(self):
        super().__init__()

    def raise_salary(seller_employee_id, amount):

        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be numeric.")

        if amount <= 0:
            raise ValueError("Raise amount must be greater than zero.")

        employee = MySQLProgramQueries.get_employee_query(seller_employee_id, "seller_employee")

        if employee is not None and employee["salary"] + amount > 100000:
            raise ValueError("Salary can't be greater than 100000.")

        return MySQLProgramQueries.raise_employee_salary_query(amount, seller_employee_id, "seller_employee")

    @staticmethod
    def hire_employee(new_employee):
        return MySQLProgramQueries.add_employee_query(
            new_employee.firstname,
            new_employee.lastname,
            new_employee.username,
            new_employee.password,
            new_employee.age,
            new_employee.phone_num,
            new_employee.address,
            new_employee.bank_account_num,
            new_employee.salary,
            "seller_employee"
        )

    @staticmethod
    def fire_employee(seller_employee_id):
        return MySQLProgramQueries.delete_employee_query(seller_employee_id, "seller_employee")

    @staticmethod
    def get_seller_employees():
        return MySQLProgramQueries.get_all_employees_query("seller_employee")

    @staticmethod
    def get_seller_employee_byID(seller_employee_id):
        return MySQLProgramQueries.get_employee_query(seller_employee_id, "seller_employee")

    # @staticmethod
    # def check_employee_byID(emp_id):
    #     seller_employees = SellerManager.get_seller_employees()
    #     for se in seller_employees:
    #         if se["id"] == emp_id:
    #             return True
    #     return False
