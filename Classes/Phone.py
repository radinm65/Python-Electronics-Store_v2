from Classes.Product import Product
from FileCommands import FileCommands


class Phone(Product):

    def __init__(self):
        super().__init__()
        self.__ram_gb = None
        self.__storage_gb = None
        self.__battery_mah = None

    @property
    def category(self):
        return "Phone"

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
    def battery_mah(self):
        return self.__battery_mah

    @battery_mah.setter
    def battery_mah(self, new_battery_mah):
        try:
            new_battery_mah = int(new_battery_mah)
        except ValueError:
            raise ValueError("Battery capacity must be a whole number.")

        if not (500 <= new_battery_mah <= 10000):
            raise ValueError("Battery capacity (mAh) must be between 500 and 10000.")
        self.__battery_mah = new_battery_mah


    def extra_fields(self):
        return {
            "ram_gb": self.ram_gb,
            "storage_gb": self.storage_gb,
            "battery_mah": self.battery_mah,
        }

    @classmethod
    def from_dict(cls, product_data):
        phone = cls()
        phone.id = product_data["id"]
        phone.seller_id = product_data["seller_id"]
        phone.name = product_data["name"]
        phone.brand = product_data["brand"]
        phone.price = product_data["price"]
        phone.ram_gb = product_data["ram_gb"]
        phone.storage_gb = product_data["storage_gb"]
        phone.battery_mah = product_data["battery_mah"]

        return phone

    @staticmethod
    def get_approved_products():
        return FileCommands.get_file_data("./Database/ApprovedPhones.json")

    @staticmethod
    def get_product_byID(product_id):
        return next(
            (p for p in Phone.get_approved_products() if p["id"] == product_id), None
        )

    @staticmethod
    def edit_product(json_product):
        return FileCommands.edit_data("./Database/ApprovedPhones.json", json_product)

    @staticmethod
    def remove_product(product_id):
        return FileCommands.delete_data("./Database/ApprovedPhones.json", product_id)

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Brand: {self.brand}\n"
            f"Price: {self.price}\n"
            f"Category: {self.category}\n"
            f"RAM (GB): {self.ram_gb}\n"
            f"Storage (GB): {self.storage_gb}\n"
            f"Battery Capacity (mAh): {self.battery_mah}\n"
            f"Made By ID: {self.seller_id}\n"
            f"Date Created: {self.date_created}\n"
        )
