from Classes.User import User
from Database.MySQLProgramQueries import MySQLProgramQueries


class Seller(User):
    def __init__(self):
        super().__init__()
        self.id = None

    def save(self):
        return MySQLProgramQueries.add_seller_query(
            self.firstname,
            self.lastname,
            self.username,
            self.password,
            self.age,
            self.phone_num,
            self.address,
            self.balance,
        )

    # //! Returns p.* and all camera, laptop, phone fields
    def get_seller_unapproved_products(self):
        return MySQLProgramQueries.get_Seller_pending_products_query(self.id)

    # //! seller_json was replaced by seller_id
    @staticmethod
    def delete_product_from_seller(seller_id, product_id):
        return MySQLProgramQueries.delete_seller_product_query(product_id, seller_id)

    @classmethod
    def from_data(cls, data):
        seller = cls()
        seller.id = data["id"]
        seller.firstname = data["firstname"]
        seller.lastname = data["lastname"]
        seller.username = data["username"]
        seller.set_hashed_password(data["password"])
        seller.age = str(data["age"])
        seller.phone_num = data["phone_num"]
        seller.address = data["address"]
        seller.balance = data["balance"]
        return seller

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Firstname: {self.firstname}\n"
            f"Lastname: {self.lastname}\n"
            f"Username: {self.username}\n"
            f"Age: {self.age}\n"
            f"Phone_num: {self.phone_num}\n"
            f"Address: {self.address}\n"
            f"Balance: {self.balance}\n"
        )
