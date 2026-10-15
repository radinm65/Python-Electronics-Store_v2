from Classes.Person import Person
from abc import abstractmethod
from datetime import datetime


class Employee(Person):
    def __init__(self):
        super().__init__()
        self.date_hired = datetime.today()
        self.__bank_account_num = None
        self.__salary = None

    @property
    def bank_account_num(self):
        return self.__bank_account_num

    @bank_account_num.setter
    def bank_account_num(self, value):
        value = str(value)

        if not value.isdigit():
            raise ValueError("Bank account must contain only numbers.")

        if len(value) < 10:
            raise ValueError("Bank account number is too short.")

        self.__bank_account_num = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Salary must be numeric.")

        if value < 0:
            raise ValueError("Salary can't be negative.")

        self.__salary = value

    @staticmethod
    @abstractmethod
    def answer_ticket():
        pass
