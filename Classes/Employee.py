from Classes.Person import Person
from abc import abstractmethod
from datetime import datetime
from Database.MySQLProgramQueries import MySQLProgramQueries

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.date_hired = None
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

        if len(value) != 16:
            raise ValueError("Bank account number must have 16 digits.")

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

        if value > 100000:
            raise ValueError("Salary can't be greater than 100000.")

        self.__salary = value

    @staticmethod
    def answer_ticket(ticket_id, answer):
        if len(answer.strip()) < 10:
            raise ValueError("Ticket response must be at least 10 characters.")

        return MySQLProgramQueries.answer_ticket_query(ticket_id, answer) 
