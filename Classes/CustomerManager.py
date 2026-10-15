from Classes.Manager import Manager
from FileCommands import FileCommands
from Classes.CustomerEmployee import CustomerEmployee


class CustomerManager(Manager):
    def __init__(self):
        super().__init__()

    def raise_salary(customers_employee_id, amount):

        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be numeric.")

        if amount <= 0:
            raise ValueError("Raise amount must be greater than zero.")

        customer_employees = CustomerManager.get_customer_employees()
        for ce in customer_employees:
            if ce["id"] == customers_employee_id:
                ce["salary"] += amount
                return CustomerManager.save_customer_employees(customer_employees)
        return False

    @staticmethod
    def hire_employee(new_customer):
        json_customer = {
            "id": new_customer.id,
            "firstname": new_customer.firstname,
            "lastname": new_customer.lastname,
            "username": new_customer.username,
            "password": new_customer.password,
            "age": new_customer.age,
            "phone_num": new_customer.phone_num,
            "address": new_customer.address,
            "bank_account_num": new_customer.bank_account_num,
            "date_hired": new_customer.date_hired.isoformat(),
            "salary": new_customer.salary
        }
        return FileCommands.add_data("./Database/CustomerEmployees.json", json_customer)

    @staticmethod
    def fire_employee(customers_employee_id):
        return FileCommands.delete_data("./Database/CustomerEmployees.json", customers_employee_id)

    @staticmethod
    def get_customer_employees():
        return FileCommands.get_file_data("./Database/CustomerEmployees.json")

    @staticmethod
    def get_customer_employee_byID(customer_employee_id):
        customer_employees = CustomerManager.get_customer_employees()
        found_ce = next(
            (ce for ce in customer_employees if ce["id"] == customer_employee_id), None
        )
        return found_ce


    @staticmethod
    def save_customer_employees(customer_employees):
        return FileCommands.save_file_data("./Database/CustomerEmployees.json", customer_employees)

    @staticmethod
    def check_employee_byID(emp_id):
        customer_employees = CustomerManager.get_customer_employees()
        for ce in customer_employees:
            if ce["id"] == emp_id:
                return True
        return False
