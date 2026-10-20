from Classes.Manager import Manager
from Database.MySQLProgramQueries import MySQLProgramQueries


class CustomerManager(Manager):
    def __init__(self):
        super().__init__()

    def raise_salary(customers_employee_id, amount):
        
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be numeric.")

        if amount <= 0:
            raise ValueError("Raise amount must be greater than zero.")

        employee = MySQLProgramQueries.get_employee_query(customers_employee_id, "customer_employee")

        if employee is not None and employee["salary"] + amount > 100000:
            raise ValueError("Salary can't be greater than 100000.")

        return MySQLProgramQueries.raise_employee_salary_query(amount, customers_employee_id, "customer_employee")

    @staticmethod
    def hire_employee(new_customer):
        return MySQLProgramQueries.add_employee_query(
            new_customer.firstname,
            new_customer.lastname,
            new_customer.username,
            new_customer.password,
            new_customer.age,
            new_customer.phone_num,
            new_customer.address,
            new_customer.bank_account_num,
            new_customer.salary,
            "customer_employee",
        )

    @staticmethod
    def fire_employee(customers_employee_id):
        return MySQLProgramQueries.delete_employee_query(customers_employee_id, "customer_employee")

    @staticmethod
    def get_customer_employees():
        return MySQLProgramQueries.get_all_employees_query("customer_employee")

    @staticmethod
    def get_customer_employee_byID(customer_employee_id):
        return MySQLProgramQueries.get_employee_query(customer_employee_id, "customer_employee")


    # @staticmethod
    # def check_employee_byID(emp_id):
    #     customer_employees = CustomerManager.get_customer_employees()
    #     for ce in customer_employees:
    #         if ce["id"] == emp_id:
    #             return True
    #     return False
