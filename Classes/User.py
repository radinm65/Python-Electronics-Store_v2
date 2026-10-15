from Classes.Person import Person
from Classes.Ticket import Ticket


class User(Person):
    def __init__(self):
        super().__init__()
        self.balance = 0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Balance must be numeric.")

        if value < 0:
            raise ValueError("Balance can't be negative.")

        self.__balance = value

    @staticmethod
    def get_user_tickets(user_id, sender_type):
        user_tickets = []
        if sender_type == "customer":
            tickets = Ticket.get_sellers_tickets()
        else:
            tickets = Ticket.get_customers_tickets()

        for ticket in tickets:
            if ticket["from_id"] == user_id:
                user_tickets.append(ticket)
        return user_tickets
