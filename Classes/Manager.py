from Classes.Person import Person
from abc import abstractmethod


class Manager(Person):
    def __init__(self):
        super().__init__()

    @staticmethod
    @abstractmethod
    def raise_salary():
        pass

    @staticmethod
    @abstractmethod
    def hire_employee():
        pass

    @staticmethod
    @abstractmethod
    def fire_employee():
        pass
