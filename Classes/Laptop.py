from Classes.Product import Product
from FileCommands import FileCommands


class Laptop(Product):

    def __init__(self):
        super().__init__()
        self.__ram_gb = None
        self.__storage_gb = None
        self.__cpu = None

    @property
    def category(self):
        return "Laptop"

    @property
    def ram_gb(self):
        return self.__ram_gb

    @ram_gb.setter
    def ram_gb(self, new_ram_gb):
        try:
            new_ram_gb = int(new_ram_gb)
        except ValueError:
            raise ValueError("RAM must be a whole number.")

        if not (1 <= new_ram_gb <= 256):
            raise ValueError("RAM (GB) must be between 1 and 256.")
        self.__ram_gb = new_ram_gb

    @property
    def storage_gb(self):
        return self.__storage_gb

    @storage_gb.setter
    def storage_gb(self, new_storage_gb):
        try:
            new_storage_gb = int(new_storage_gb)
        except ValueError:
            raise ValueError("Storage must be a whole number.")

        if not (1 <= new_storage_gb <= 8192):
            raise ValueError("Storage (GB) must be between 1 and 8192.")
        self.__storage_gb = new_storage_gb

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, new_cpu):
        if len(new_cpu) < 2:
            raise ValueError("CPU should be longer than 2 characters.")
        self.__cpu = new_cpu

    def extra_fields(self):
        return {
            "ram_gb": self.ram_gb,
            "storage_gb": self.storage_gb,
            "cpu": self.cpu,
        }

    @classmethod
    def from_dict(cls, product_data):
        laptop = cls()
        laptop.id = product_data["id"]
        laptop.seller_id = product_data["seller_id"]
        laptop.name = product_data["name"]
        laptop.brand = product_data["brand"]
        laptop.price = product_data["price"]
        laptop.ram_gb = product_data["ram_gb"]
        laptop.storage_gb = product_data["storage_gb"]
        laptop.cpu = product_data["cpu"]

        return laptop

    @staticmethod
    def get_approved_products():
        return FileCommands.get_file_data("./Database/ApprovedLaptops.json")

    @staticmethod
    def get_product_byID(product_id):
        return next(
            (p for p in Laptop.get_approved_products() if p["id"] == product_id), None
        )

    @staticmethod
    def edit_product(json_product):
        return FileCommands.edit_data("./Database/ApprovedLaptops.json", json_product)

    @staticmethod
    def remove_product(product_id):
        return FileCommands.delete_data("./Database/ApprovedLaptops.json", product_id)

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Brand: {self.brand}\n"
            f"Price: {self.price}\n"
            f"Category: {self.category}\n"
            f"RAM (GB): {self.ram_gb}\n"
            f"Storage (GB): {self.storage_gb}\n"
            f"CPU: {self.cpu}\n"
            f"Made By ID: {self.seller_id}\n"
            f"Date Created: {self.date_created}\n"
        )
