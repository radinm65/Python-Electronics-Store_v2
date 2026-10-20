from datetime import datetime
from Database.MySQLProgramQueries import MySQLProgramQueries


class Ticket:

    def __init__(self):
        self.id = None
        self.from_id = None
        self.response = None
        self.__date_created = None

    @property
    def request(self):
        return self.__request

    @request.setter
    def request(self, new_request):
        if len(new_request) > 200:
            raise ValueError("Ticket request must be under 200 characters.")

        if len(new_request) < 10:
            raise ValueError("Ticket request must be at least 10 characters.")
        self.__request = new_request

    @property
    def from_name(self):
        return self.__from_name

    @from_name.setter
    def from_name(self, new_from_name):
        if len(new_from_name) < 3:
            raise ValueError("Name must be at least 3 characters.")

        if any(char.isdigit() for char in new_from_name):
            raise ValueError("Name shouldn't have numbers.")
        self.__from_name = new_from_name

    @property
    def date_created(self):
        return self.__date_created

    @property
    def sender_type(self):
        return self.__sender_type

    @sender_type.setter
    def sender_type(self, new_type):
        if new_type not in ("customer", "seller"):
            raise ValueError("Sender type must be customer or seller.")
        self.__sender_type = new_type

    def save(self):
        return MySQLProgramQueries.add_ticket_query(
            self.from_name, self.from_id, self.sender_type, self.request
        )

    @staticmethod
    def get_all_tickets():
        return MySQLProgramQueries.get_all_tickets_query()

    @staticmethod
    def get_sendertype_tickets(sender_type):
        return MySQLProgramQueries.get_sender_type_tickets_query(sender_type)

    @staticmethod
    def get_unanswered_sendertype_tickets(sender_type):
        return MySQLProgramQueries.get_unanswered_sender_type_tickets_query(sender_type)

    # @staticmethod
    # def check_unanswered_ticketID(ticketID, sender_type):
    #     unanswered_tickets = Ticket.get_unanswered_sendertype_tickets(sender_type)
    #     for ut in unanswered_tickets:
    #         if ticketID == ut["id"]:
    #             return True
    #     return False

    @staticmethod
    def get_user_tickets(user_id, sender_type):
        return MySQLProgramQueries.get_user_tickets_query(sender_type, user_id)

    @staticmethod
    def from_dict(ticket_dict):
        ticket = Ticket()
        ticket.id = ticket_dict["id"]
        ticket.from_id = ticket_dict["from_id"]
        ticket.from_name = ticket_dict["from_name"]
        ticket.request = ticket_dict["request"]
        ticket.sender_type = ticket_dict["sender_type"]
        ticket.response = ticket_dict.get("response", "")

        return ticket

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"From: {self.from_name}\n"
            f"From ID: {self.from_id}\n"
            f"Sender Type: {self.sender_type}\n"
            f"Request: {self.request}\n"
            f"Response: {self.response}\n"
            f"Date Created: {self.date_created}"
        )
