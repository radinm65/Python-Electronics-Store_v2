from Classes.Product import Product
from FileCommands import FileCommands


class Camera(Product):

    def __init__(self):
        super().__init__()
        self.__resolution_mp = None
        self.__zoom_factor = None
        self.__sensor_type = None

    @property
    def category(self):
        return "Camera"

    @property
    def resolution_mp(self):
        return self.__resolution_mp

    @resolution_mp.setter
    def resolution_mp(self, new_resolution_mp):
        try:
            new_resolution_mp = float(new_resolution_mp)
        except ValueError:
            raise ValueError("Resolution must be numeric.")

        if not (0.1 <= new_resolution_mp <= 200):
            raise ValueError("Resolution (MP) must be between 0.1 and 200.")
        self.__resolution_mp = new_resolution_mp

    @property
    def zoom_factor(self):
        return self.__zoom_factor

    @zoom_factor.setter
    def zoom_factor(self, new_zoom_factor):
        try:
            new_zoom_factor = float(new_zoom_factor)
        except ValueError:
            raise ValueError("Zoom factor must be numeric.")

        if not (1 <= new_zoom_factor <= 100):
            raise ValueError("Zoom factor must be between 1 and 100.")
        self.__zoom_factor = new_zoom_factor

    @property
    def sensor_type(self):
        return self.__sensor_type

    @sensor_type.setter
    def sensor_type(self, new_sensor_type):
        if len(new_sensor_type) < 2:
            raise ValueError("Sensor type should be longer than 2 characters.")
        self.__sensor_type = new_sensor_type


    def extra_fields(self):
        return {
            "resolution_mp": self.resolution_mp,
            "zoom_factor": self.zoom_factor,
            "sensor_type": self.sensor_type,
        }

    @classmethod
    def from_dict(cls, product_data):
        camera = cls()
        camera.id = product_data["id"]
        camera.seller_id = product_data["seller_id"]
        camera.name = product_data["name"]
        camera.brand = product_data["brand"]
        camera.price = product_data["price"]
        camera.resolution_mp = product_data["resolution_mp"]
        camera.zoom_factor = product_data["zoom_factor"]
        camera.sensor_type = product_data["sensor_type"]

        return camera

    @staticmethod
    def get_approved_products():
        return FileCommands.get_file_data("./Database/ApprovedCameras.json")

    @staticmethod
    def get_product_byID(product_id):
        return next(
            (p for p in Camera.get_approved_products() if p["id"] == product_id), None
        )

    @staticmethod
    def edit_product(json_product):
        return FileCommands.edit_data("./Database/ApprovedCameras.json", json_product)

    @staticmethod
    def remove_product(product_id):
        return FileCommands.delete_data("./Database/ApprovedCameras.json", product_id)

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Brand: {self.brand}\n"
            f"Price: {self.price}\n"
            f"Category: {self.category}\n"
            f"Resolution (MP): {self.resolution_mp}\n"
            f"Zoom Factor: {self.zoom_factor}\n"
            f"Sensor Type: {self.sensor_type}\n"
            f"Made By ID: {self.seller_id}\n"
            f"Date Created: {self.date_created}\n"
        )
