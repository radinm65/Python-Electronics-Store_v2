from abc import ABC
import re
import hashlib
from FileCommands import FileCommands


class Person(ABC):
    def __init__(self):
        self.__firstname = None
        self.__lastname = None
        self.__username = None
        self.__password = None
        self.__age = None
        self.__phone_num = None
        self.__address = None

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, new_firstname):
        if len(new_firstname) < 3:
            raise ValueError("Firstname can't be shorter than 3 characters.")

        if any(char.isdigit() for char in new_firstname):
            raise ValueError("Firstname shouldn't have numbers.")

        self.__firstname = new_firstname

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, new_lastname):
        if len(new_lastname) < 3:
            raise ValueError("Lastname can't be shorter than 3 characters.")

        if any(char.isdigit() for char in new_lastname):
            raise ValueError("Lastname shouldn't have numbers.")

        self.__lastname = new_lastname

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5:
            raise ValueError("Username can't be shorter than 5 characters.")

        if not any(char.isdigit() for char in value):
            raise ValueError("Username should have numbers.")

        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if len(new_password) < 8:
            raise ValueError("Password too short.")

        if sum(char.isdigit() for char in new_password) < 3:
            raise ValueError("Password needs 3 numbers.")

        if not new_password[0].isupper():
            raise ValueError("Password needs capital letter.")

        if not re.search(r"[^a-zA-Z0-9]", new_password):
            raise ValueError("Password needs special character.")

        self.__password = hashlib.sha256(new_password.encode()).hexdigest()

    def set_hashed_password(self, hashed_password):
        self.__password = hashed_password

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not new_age.isdigit():
            raise ValueError("Age must be numeric.")

        if int(new_age) > 80:
            raise ValueError("Age cannot be above 80.")

        self.__age = int(new_age)

    @property
    def phone_num(self):
        return self.__phone_num

    @phone_num.setter
    def phone_num(self, new_num):
        if len(new_num) != 10:
            raise ValueError("Phone must have 10 digits.")

        if not new_num.isdigit():
            raise ValueError("Phone must be numeric.")

        self.__phone_num = new_num

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if len(value) < 10:
            raise ValueError("Address is too short.")

        self.__address = value

    def get_hash_Password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_login(file_path, input_username, input_password):
        hashed_password = hashlib.sha256(input_password.encode()).hexdigest()
        get_users = FileCommands.get_file_data(file_path)

        if len(get_users) == 0:
            raise ValueError("No users of this type have been registered yet")
        for user in get_users:
            if hashed_password == user["password"] and input_username == user["username"]:
                return True, user

        return False, None
