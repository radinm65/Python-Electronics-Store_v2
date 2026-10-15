import colorama
from Classes.CustomerManager import CustomerManager
from Classes.SellerManager import SellerManager
from Classes.Person import Person
from Classes.Customer import Customer
from Classes.Seller import Seller
from Classes.CustomerEmployee import CustomerEmployee
from Classes.SellerEmployee import SellerEmployee
from Classes.Product import Product
from Classes.Phone import Phone
from Classes.Laptop import Laptop
from Classes.Camera import Camera
from Classes.Ticket import Ticket
from Report import Report


def print_error(message):
    print(colorama.Fore.RED)
    print(message, colorama.Fore.WHITE)


def print_successful(message):
    print(colorama.Fore.GREEN)
    print(message, colorama.Fore.WHITE)


# Show Menus -------------------


def show_main_menu():
    print(
        colorama.Fore.YELLOW,
        "\nWelcome!\n\n"
        "1- Customer\n"
        "2- Seller\n"
        "3- Customer Employee\n"
        "4- Seller Employee\n"
        "5- Customer Manager\n"
        "6- Seller Manager\n"
        "7- Exit\n\n",
        colorama.Fore.WHITE,
    )


def show_customer_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Shop\n" "2- Tickets\n" "3- Account Info\n" "4- Back\n", colorama.Fore.WHITE
    )


def show_customer_shop_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Checkout\n"
        "2- Filter products\n"
        "3- Add to Cart\n"
        "4- Add To Favorites\n"
        "5- Add Favorites To cart\n"
        "6- Delete From Cart\n"
        "7- Delete From Favorites\n"
        "8- See Cart and Favorites\n"
        "9- Add to balance\n"
        "10- Back\n",
        colorama.Fore.WHITE,
    )


def show_ticket_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Submit Ticket\n" "2- See Submited tickets\n" "3- Back\n",
        colorama.Fore.WHITE,
    )


def show_seller_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Products Menu\n" "2- Tickets Menu\n" "3- Account Info\n" "4- Back\n",
        colorama.Fore.WHITE,
    )


def show_seller_product_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Make Product\n"
        "2- See Selling Products\n"
        "3- See Unapproved Products\n"
        "4- Delete Products from selling list\n"
        "5- Edit Product\n"
        "6- Back\n",
        colorama.Fore.WHITE,
    )


def show_customer_employee_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Tickets Panel\n" "2- Remove Customer\n" "3- Account Info\n" "4- Back\n",
        colorama.Fore.WHITE,
    )


def show_employee_Ticket_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Answer Ticket\n" "2- See all tickets\n" "3- Back\n",
        colorama.Fore.WHITE,
    )


def show_seller_employee_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Seller managing\n"
        "2- Product managing\n"
        "3- Ticket managing\n"
        "4- See Account Info\n"
        "5- Back\n",
        colorama.Fore.WHITE,
    )


def show_seller_employee_seller_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Approve seller\n" "2- Remove seller\n" "3- Back\n",
        colorama.Fore.WHITE,
    )


def show_seller_employee_product_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Approve product\n" "2- Remove product\n" "3- Edit product\n" "4- Back\n",
        colorama.Fore.WHITE,
    )


def show_customer_employee_manager_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Hire Customer Employee\n"
        "2- Fire Customer Employee\n"
        "3- Give Raise\n"
        "4- See All Customer Employees\n"
        "5- See All Customers\n"
        "6- Get top 3 Customers .xlsx Report\n"
        "7- Get customers CSV or TXT report\n"
        "8- See Account Info\n"
        "9- Back\n",
        colorama.Fore.WHITE,
    )


def show_seller_employee_manager_menu():
    print(colorama.Fore.YELLOW)
    print(
        "1- Hire seller Employee\n"
        "2- Fire seller Employee\n"
        "3- Give Raise\n"
        "4- See All seller Employees\n"
        "5- See All sellers\n"
        "6- Get top 3 sellers .xlsx Report\n"
        "7- Get sellers CSV or TXT report\n"
        "8- See Account Info\n"
        "9- Back\n",
        colorama.Fore.WHITE,
    )


# Fuctions and Methods -----------------------------------------------------------------------------------

# Joined Managers Functions -----------------------


def hire_employee(employee_type):
    while True:
        try:
            print_error("Enter 'e' on first input to exit\n")

            firstname = input("Enter Firstname:\n")
            if firstname == "e":
                print_successful("Exited Hiring!\n")
                return True

            if employee_type == "customer":
                new_employee = CustomerEmployee()
            else:
                new_employee = SellerEmployee()

            new_employee.firstname = firstname

            new_employee.lastname = input("Enter Lastname:\n")

            new_employee.username = input("Enter Username:\n")

            new_employee.password = input("Enter Password:\n")

            new_employee.age = input("Enter age:\n")

            new_employee.phone_num = input("Enter Phone number:\n")

            new_employee.address = input("Enter Address:\n")

            new_employee.bank_account_num = input("Enter Bank Account Number:\n")

            new_employee.salary = int(input("Enter Salary:\n"))

            if employee_type == "customer":
                CustomerManager.hire_employee(new_employee)
                print_successful("Customer Employee has Been Hired Successfully!")

            elif employee_type == "seller":
                SellerManager.hire_employee(new_employee)
                print_successful("Seller Employee has Been Hired Successfully!")

            break

        except ValueError as e:
            print_error(e)
            continue


def fire_employee(employee_type):
    try:
        emp_id = int(input(f"\nEnter {employee_type} Employee ID to Fire:\n"))
        if employee_type == "customer":
            if CustomerManager.fire_employee(emp_id):
                print_successful("Customer Employee is Fired!")
        elif employee_type == "seller":
            if SellerManager.fire_employee(emp_id):
                print_successful("Seller Employee is Fired!")
    except Exception as e:
        print_error(e)


def give_employee_raise(employee_type):
    try:
        success = False
        emp_id = int(input("\nEnter Customer Employee ID to Give Raise:\n"))
        if employee_type == "customer":
            if CustomerManager.check_employee_byID(emp_id):
                salary_raise = int(input("How much raise?\n"))
                CustomerManager.raise_salary(emp_id, salary_raise)
                success = True
            else:
                print_error("No Such ID Was Found")

        elif employee_type == "seller":

            if SellerManager.check_employee_byID(emp_id):
                salary_raise = int(input("How much raise?\n"))
                SellerManager.raise_salary(emp_id, salary_raise)
                success = True
            else:
                print_error("No Such ID Was Found")
        if success:
            print_successful(f"{employee_type} Employee was given a raise!")

    except Exception as e:
        print_error(e)


def show_all_employees(employee_type):
    if employee_type == "customer":
        employees = CustomerManager.get_customer_employees()

    elif employee_type == "seller":
        employees = SellerManager.get_seller_employees()

    if len(employees) == 0:
        print_error(f"No {employee_type} employees have been registered.")
        return

    for emp in employees:
        print(colorama.Fore.BLUE)
        print(
            f"ID: {emp['id']}\n"
            f"Firstname: {emp['firstname']}\n"
            f"Lastname: {emp['lastname']}\n"
            f"Username: {emp['username']}\n"
            f"Password: *********\n"
            f"Age: {emp['age']}\n"
            f"Phone_num: {emp['phone_num']}\n"
            f"Address: {emp['address']}\n"
            f"Bank account Number: {emp['bank_account_num']}\n"
            f"Date Hired: {emp['date_hired']}\n"
            f"Salary: {emp['salary']}\n"
        )

    print(colorama.Fore.WHITE)


def show_all_users(user_type):
    if user_type == "customer":
        users = CustomerEmployee.get_customers()

    elif user_type == "seller":
        users = SellerEmployee.get_sellers()

    else:
        print_error("Invalid user type.")
        return

    if len(users) == 0:
        print_error(f"No {user_type}s have been registered.")
        return

    for user in users:
        print(colorama.Fore.BLUE)
        if user_type == "customer":
            print(Customer.from_dict(user))
        elif user_type == "seller":
            print(Seller.from_dict(user))

    print(colorama.Fore.WHITE)


def generate_top3_report(employee_type):
    successfull = False
    if employee_type == "customer":
        if len(CustomerEmployee.get_customers()) < 5:
            print_error("Not enough data for report to generate.")
        else:
            try:
                if Report.generate_top_customers_report():
                    successfull = True
            except Exception as e:
                print_error(e)
    elif employee_type == "seller":
        if len(SellerEmployee.get_sellers()) < 5:
            print_error("Not enough data for report to generate.")
        else:
            try:
                if Report.generate_top_sellers_report():
                    successfull = True
            except Exception as e:
                print_error(e)

    if successfull:
        print_successful("Generated Succesfully")


def show_manager_account_info(manager):
    print(colorama.Fore.BLUE)
    print(
        f"Firstname: {manager.firstname}\n"
        f"Lastname: {manager.lastname}\n"
        f"Username: {manager.username}\n"
        f"Age: {manager.age}\n"
        f"Phone_num: {manager.phone_num}\n"
        f"Address: {manager.address}\n",
        colorama.Fore.WHITE,
    )


def login_user(username, password, usertype, managers):

    users = {
        "customer": {
            "file": "./Database/Customers.json",
            "class": Customer,
            "panel": customers_panel,
            "can_signup": True,
        },
        "seller": {
            "file": "./Database/Sellers.json",
            "class": Seller,
            "panel": sellers_panel,
            "can_signup": True,
        },
        "customer_employee": {
            "file": "./Database/CustomerEmployees.json",
            "class": CustomerEmployee,
            "panel": customer_employee_panel,
            "can_signup": False,
        },
        "seller_employee": {
            "file": "./Database/SellerEmployees.json",
            "class": SellerEmployee,
            "panel": seller_employee_panel,
            "can_signup": False,
        },
        "customer_manager": {
            "object": managers["customer"],
            "panel": show_employee_manager_panel,
            "panel_args": "customer",
            "can_signup": False,
        },
        "seller_manager": {
            "object": managers["seller"],
            "panel": show_employee_manager_panel,
            "panel_args": "seller",
            "can_signup": False,
        },
    }

    try:
        user_data = users[usertype]

        if "object" in user_data:

            manager = user_data["object"]

            if (
                manager.username == username
                and manager.password == Person.get_hash_Password(password)
            ):
                user_data["panel"](manager, user_data["panel_args"])
                return True

            print_error("Wrong Username or Password.")
            return False

        login, user = Person.check_login(user_data["file"], username, password)

        if login:

            user_obj = user_data["class"].from_dict(user)

            user_data["panel"](user_obj)

            return True

        print_error("Wrong Username or Password.")

        if not user_data["can_signup"]:
            return False

        while True:

            signup_choice = input("\nDo you have an Account?\n" "1- Yes\n" "2- No\n")

            if signup_choice == "1":
                return False

            elif signup_choice == "2":

                signedup, new_user = signup_user(usertype)

                if signedup:
                    if usertype == "customer":
                        user_data["panel"](new_user)
                    return True

            else:
                print_error("Please only choose from options.")

    except ValueError as e:
        print_error(e)
        return False

    except KeyError:
        print_error("Invalid user type.")
        return False


def signup_user(signup_type):
    try:
        print_error("Enter 'e' on first input to exit\n")

        firstname = input("Enter Firstname:\n")
        if firstname == "e":
            print_successful("Exited signup!\n")
            return False, None

        if signup_type == "customer":
            user = Customer()
            user.cart = []
            user.favorites = []
            user.bought = []
        elif signup_type == "seller":
            user = Seller()
            user.selling_products = []
            user.sold = []

        user.firstname = firstname

        user.lastname = input("Enter Lastname:\n")

        username = input("Enter Username:\n")

        if signup_type == "customer":
            for customer in CustomerEmployee.get_customers():
                if customer["username"] == username:
                    raise ValueError("Username already exists.")
        elif signup_type == "seller":
            for seller in SellerEmployee.get_sellers():
                if seller["username"] == username:
                    raise ValueError("Username already exists.")

        user.username = username

        user.password = input("Enter Password:\n")

        user.age = input("Enter age:\n")

        user.phone_num = input("Enter Phone number:\n")

        user.address = input("Enter Address:\n")

        user.save()

        if signup_type == "customer":
            print_successful("Customer Signed up Successfully!")

        elif signup_type == "seller":
            print_successful(
                "Seller signed up Successfully!\nAfter Being Approved, you can signin"
            )
        return True, user

    except ValueError as e:
        print_error(e)
        return False, None


def show_products():
    try:
        phones = Phone.get_approved_products()
        laptops = Laptop.get_approved_products()
        cameras = Camera.get_approved_products()
        print(colorama.Fore.BLUE)
        for phone in phones:
            print(Phone.from_dict(phone))
        for laptop in laptops:
            print(Laptop.from_dict(laptop))
        for camera in cameras:
            print(Camera.from_dict(camera))
        print(colorama.Fore.WHITE)

    except ValueError as e:
        print_error(e)


def handle_customer_add_actions(customer, method):

    actions = {"cart": customer.add_to_cart, "favorites": customer.add_to_favorites}

    messages = {
        "cart": "Enter Product ID To Add to cart:\n",
        "favorites": "Enter Product ID To Add to favorites:\n",
    }

    while True:
        try:
            print_error("enter e to exit")
            product_id = input(messages[method])

            if product_id == "e":
                break
            elif not product_id.isdigit():
                print_error("Enter number for ID.")
                continue

            product_id = int(product_id)

            successful = actions[method](product_id)

            if not successful:
                print_error("Failed To do task")
                continue

            again = input("Anything Else?\n1- Yes\n")

            if again != "1":
                break

        except ValueError as e:
            print_error(e)


def handle_customer_remove_actions(customer, method):

    actions = {
        "cart": customer.remove_from_cart,
        "favorites": customer.remove_from_favorites,
    }

    messages = {
        "cart": "Enter Product ID To remove from cart:\n",
        "favorites": "Enter Product ID To remove from favorites:\n",
    }

    if method not in actions:
        print_error("Invalid remove action")

    while True:
        try:
            print_error("enter e to exit")
            product_id = input(messages[method])
            if product_id == "e":
                break

            product_id = int(product_id)
            successful = actions[method](product_id)

            if successful:
                print_successful("Removed Successfully")
            else:
                print_error("Failed To do task")

            again = input("Anything Else?\n1- Yes\n2- No\n")

            if again != "1":
                break

        except ValueError as e:
            print_error(e)


def show_customer_cart_and_favorites(customer_id):
    print(colorama.Fore.BLUE)

    customer = CustomerEmployee.get_customer_byID(customer_id)

    print("\n========== CART ==========")

    if len(customer["cart"]) == 0:
        print("Your cart is empty.")
    else:
        for product_id in customer["cart"]:
            product = Product.get_product_byID(product_id)

            if product:
                print(
                    f"ID: {product['id']}\n"
                    f"Name: {product['name']}\n"
                    f"Brand: {product['brand']}\n"
                    f"Price: {product['price']}\n"
                    f"Category: {product['category']}\n"
                    f"-------------------------\n"
                )

    # Favorites
    print("\n======== FAVORITES ========")

    if len(customer["favorites"]) == 0:
        print("Your favorites are empty.")
    else:
        for product_id in customer["favorites"]:
            product = Product.get_product_byID(product_id)

            if product:
                print(
                    f"ID: {product['id']}\n"
                    f"Name: {product['name']}\n"
                    f"Brand: {product['brand']}\n"
                    f"Price: {product['price']}\n"
                    f"Category: {product['category']}\n"
                    f"-------------------------\n"
                )

    print(colorama.Fore.WHITE)


def add_cart_to_favorites(customer):
    try:
        if Customer.add_cart_to_favorites(customer.id):
            print_successful("Favorites added to cart successfully!")
        else:
            print_error("Customer not found.")

    except ValueError as e:
        print_error(e)


def submit_ticket(user, sender_type):
    try:
        new_ticket = Ticket()
        new_ticket.from_id = user.id
        new_ticket.response = ""
        new_ticket.from_name = user.firstname
        new_ticket.request = input("What is the problem?\n")
        new_ticket.sender_type = sender_type
        new_ticket.save()
        print_successful("New Ticket Submitted")
    except ValueError as e:
        print_error(e)


def see_user_tickets(user, sender_type):
    try:
        user_tickets = Ticket.get_user_tickets(user.id, sender_type)

        print(colorama.Fore.BLUE)
        print("======= User Tickets =======\n")
        for ticket in user_tickets:
            ticket_obj = Ticket.from_dict(ticket)
            print(ticket_obj, end="\n\n")

    except ValueError as e:
        print_error(e)


def add_to_balance(user):
    try:
        add_balance = int(input("Enter amount to add to balance:\n"))
        customer = Customer.from_dict(CustomerEmployee.get_customer_byID(user.id))
        customer.balance = customer.balance + add_balance
        if Customer.add_to_balance(user.id, customer.balance):
            print_successful(f"Balance was added.")
        else:
            print_error("Error in adding balance.")

    except ValueError as e:
        print_error(e)


def print_account_info(user):
    print(colorama.Fore.BLUE)
    user_obj = None
    if type(user) == Customer:
        user_obj = Customer.from_dict(CustomerEmployee.get_customer_byID(user.id))
    elif type(user) == Seller:
        user_obj = Seller.from_dict(SellerEmployee.get_seller_byID(user.id))
    elif type(user) == CustomerEmployee:
        user_obj = CustomerEmployee.from_dict(
            CustomerManager.get_customer_employee_byID(user.id)
        )
    elif type(user) == SellerEmployee:
        user_obj = SellerEmployee.from_dict(
            SellerManager.get_seller_employee_byID(user.id)
        )
    print(user_obj)


def input_product_extra_fields(product):
    if type(product) == Phone:
        product.ram_gb = input("\nEnter RAM (GB):\n")
        product.storage_gb = input("\nEnter Storage (GB):\n")
        product.battery_mah = input("\nEnter Battery Capacity (mAh):\n")

    elif type(product) == Laptop:
        product.ram_gb = input("\nEnter RAM (GB):\n")
        product.storage_gb = input("\nEnter Storage (GB):\n")
        product.cpu = input("\nEnter CPU:\n")

    elif type(product) == Camera:
        product.resolution_mp = input("\nEnter Resolution (MP):\n")
        product.zoom_factor = input("\nEnter Zoom Factor (e.g. 5 for 5x):\n")
        product.sensor_type = input("\nEnter Sensor Type (e.g. CMOS, CCD):\n")


def edit_product_extra_field(product):
    if type(product) == Phone:
        print(
            "\nWhich field do you want to edit?\n"
            "1- RAM\n"
            "2- Storage\n"
            "3- Battery Capacity\n"
        )
        choice = input("Enter your choice:\n")

        match choice:
            case "1":
                product.ram_gb = input("Enter new RAM (GB):\n")
            case "2":
                product.storage_gb = input("Enter new Storage (GB):\n")
            case "3":
                product.battery_mah = input("Enter new Battery Capacity (mAh):\n")
            case _:
                raise ValueError("Invalid choice.")

    elif type(product) == Laptop:
        print(
            "\nWhich field do you want to edit?\n"
            "1- RAM\n"
            "2- Storage\n"
            "3- CPU\n"
        )
        choice = input("Enter your choice:\n")

        match choice:
            case "1":
                product.ram_gb = input("Enter new RAM (GB):\n")
            case "2":
                product.storage_gb = input("Enter new Storage (GB):\n")
            case "3":
                product.cpu = input("Enter new CPU:\n")
            case _:
                raise ValueError("Invalid choice.")

    elif type(product) == Camera:
        print(
            "\nWhich field do you want to edit?\n"
            "1- Resolution\n"
            "2- Zoom Factor\n"
            "3- Sensor Type\n"
        )
        choice = input("Enter your choice:\n")

        match choice:
            case "1":
                product.resolution_mp = input("Enter new Resolution (MP):\n")
            case "2":
                product.zoom_factor = input("Enter new Zoom Factor:\n")
            case "3":
                product.sensor_type = input("Enter new Sensor Type:\n")
            case _:
                raise ValueError("Invalid choice.")


def make_product(seller):
    while True:
        try:
            print_error("Enter e on first input to exit.\n")
            category_choice = input(
                "Choose product category:\n1- Phone\n2- Laptop\n3- Camera\n"
            )

            if category_choice == "e":
                print_successful("Exited registering product!\n")
                break

            if category_choice == "1":
                new_product = Phone()
            elif category_choice == "2":
                new_product = Laptop()
            elif category_choice == "3":
                new_product = Camera()
            else:
                print_error("Please only choose from options.")
                continue

            new_product.seller_id = seller.id

            new_product.name = input("\nEnter name of product:\n")

            new_product.brand = input("\nEnter brand:\n")

            new_product.price = input("\nEnter price:\n")

            input_product_extra_fields(new_product)

            new_product.save()

            print_successful(
                f"Product with ID {new_product.id} has been made and has to be approved.\n"
            )
            register_again = input("Register another?\n1- Yes\n")
            if register_again != "1":
                break

        except ValueError as e:
            print_error(e)


def see_seller_unapproved_products(seller):
    try:
        print(colorama.Fore.BLUE)
        print("\n====== Unapproved Products ======\n")
        unapproved_products = seller.get_seller_unapproved_products()
        for up in unapproved_products:
            if "battery_mah" in up:
                product_obj = Phone.from_dict(up)
            elif "cpu" in up:
                product_obj = Laptop.from_dict(up)
            elif "sensor_type" in up:
                product_obj = Camera.from_dict(up)
            print(product_obj, end="\n\n")
    except ValueError as e:
        print_error(e)


def see_seller_selling_products(seller):
    try:
        print(colorama.Fore.BLUE)
        print("\n====== Selling Products ======\n")
        seller_json = SellerEmployee.get_seller_byID(seller.id)
        for selling_product_id in seller_json["selling_products"]:
            product_data = Product.get_product_byID(selling_product_id)
            if product_data is None:
                continue
            if "battery_mah" in product_data:
                product_obj = Phone.from_dict(product_data)
            elif "cpu" in product_data:
                product_obj = Laptop.from_dict(product_data)
            elif "sensor_type" in product_data:
                product_obj = Camera.from_dict(product_data)
            print(product_obj, end="\n\n")
    except ValueError as e:
        print_error(e)


def delete_product_from_seller(seller):
    while True:
        try:
            product_id = input("Enter Product ID to delete (Enter 'e' to exit):\n")

            if product_id.lower() == "e":
                print_successful("Exited Deleting product!\n")
                break

            if not product_id.isdigit():
                print_error("Product ID must be a number.\n")
                continue

            product_id = int(product_id)

            seller_json = SellerEmployee.get_seller_byID(seller.id)
            if product_id not in seller_json["selling_products"]:
                print_error("This product does not belong to you.\n")
                continue
            else:
                if Seller.delete_product_from_seller(seller_json, product_id):
                    print_successful(
                        "Product was removed from your selling products successfully!\n"
                    )
                    again = input("Do you want to delete another product?\n1- Yes\n")
                    if again != "1":
                        break

        except ValueError as e:
            print_error(e)


def edit_product(seller=None):
    while True:
        try:
            product_id = input("\nEnter Product ID to edit (Enter 'e' to exit):\n")
            if product_id.lower() == "e":
                print_successful("Exited Editing product!\n")
                break
            if not product_id.isdigit():
                print_error("Product ID must be a number.\n")
                continue

            product_id = int(product_id)

            if not seller == None:
                seller_json = SellerEmployee.get_seller_byID(seller.id)
                if product_id not in seller_json["selling_products"]:
                    print_error("This product does not belong to you.\n")
                    continue

            product_data = Product.get_product_byID(product_id)
            if product_data is None:
                print_error("Invalid ID.")
                continue

            if "battery_mah" in product_data:
                product = Phone.from_dict(product_data)
            elif "cpu" in product_data:
                product = Laptop.from_dict(product_data)
            elif "sensor_type" in product_data:
                product = Camera.from_dict(product_data)

            print(
                "\nWhich field do you want to edit?\n"
                "1- Name\n"
                "2- Brand\n"
                "3- Price\n"
                "4- Type-Specific Field\n"
            )

            choice = input("Enter your choice:\n")

            match choice:
                case "1":
                    product.name = input("Enter new name:\n")

                case "2":
                    product.brand = input("Enter new brand:\n")

                case "3":
                    product.price = input("Enter new price:\n")

                case "4":
                    edit_product_extra_field(product)

                case _:
                    print_error("Invalid choice.\n")
                    continue

            edited_product = {
                "id": product.id,
                "name": product.name,
                "brand": product.brand,
                "price": product.price,
                "category": product.category,
                "seller_id": product.seller_id,
                "date_created": product_data["date_created"],
            }
            edited_product.update(product.extra_fields())

            if type(product) == Phone:
                edited = Phone.edit_product(edited_product)
            elif type(product) == Laptop:
                edited = Laptop.edit_product(edited_product)
            elif type(product) == Camera:
                edited = Camera.edit_product(edited_product)

            if edited:
                print_successful("Product was edited successfully!\n")
                again = input("Do you want to edit another product?\n1- Yes\n")
                if again != "1":
                    break

        except ValueError as e:
            print_error(e)


def remove_customer():
    while True:
        try:
            show_all_users("customer")
            customer_id = input("\nEnter Customer ID to remove (Enter 'e' to exit):\n")
            if customer_id.lower() == "e":
                print_successful("Exited deleting Customer!\n")
                break
            if not customer_id.isdigit():
                print_error("Customer ID must be a number.\n")
                continue

            customer_id = int(customer_id)

            if CustomerEmployee.delete_customer(customer_id):
                print_successful("Customer was deleted successfully!\n")
                again = input("Do you want to delete another customer?\n1- Yes\n")
                if again != "1":
                    break

        except ValueError as e:
            print_error(e)


def show_user_tickets(all_or_unanswerd, sender_type):
    try:
        if all_or_unanswerd == "all":
            user_tickets = Ticket.get_sendertype_tickets(sender_type)
        elif all_or_unanswerd == "unanswered":
            user_tickets = Ticket.get_unanswered_sendertype_tickets(sender_type)
        if len(user_tickets) == 0:
            print_successful("You have no unanswered tickets!\n")
        else:
            print(colorama.Fore.BLUE)
            print(
                f"====== {"All" if all_or_unanswerd == "all" else "Unanswered"} {sender_type}s Tickets ======\n\n"
            )
            for ut in user_tickets:
                ticket_obj = Ticket.from_dict(ut)
                print(ticket_obj, end="\n\n")
    except ValueError as e:
        print_error(e)


def answer_ticket(employee_type):
    while True:
        try:
            ticket_id = input("\nEnter ticket id to answer: (enter e to exit)\n")
            if ticket_id.lower() == "e":
                print_successful("Exited answering ticket!\n")
                break

            if not ticket_id.isdigit():
                print_error("Customer ID must be a number.\n")
                continue

            ticket_id = int(ticket_id)

            if employee_type == "customer_employee":
                user_type = "customer"
            else:
                user_type = "seller"

            if Ticket.check_unanswered_ticketID(ticket_id, user_type):
                answer = input("Enter answer for the ticket:\n")
                if employee_type == "customer_employee":
                    answered = CustomerEmployee.answer_ticket(ticket_id, answer)
                elif employee_type == "seller_employee":
                    answered = SellerEmployee.answer_ticket(ticket_id, answer)
                if answered:
                    print_successful("Ticket was answered!\n")
                    again = input("Answer another?\n1-Yes\n")
                    if again != "1":
                        break
            else:
                print_error("Invalid ticket ID.")

        except ValueError as e:
            print_error(e)


def show_unapproved_sellers():
    unapproved_sellers = SellerEmployee.get_unapproved_sellers()
    print(colorama.Fore.BLUE)
    print("======= Unapproved sellers ========")
    for us in unapproved_sellers:
        seller_obj = Seller.from_dict(us)
        print(seller_obj, end="\n---------------------\n")


def show_unapproved_products():
    unapproved_products = SellerEmployee.get_unapproved_products()
    print(colorama.Fore.BLUE)
    print("======= Unapproved products ========")
    for up in unapproved_products:
        if "battery_mah" in up:
            product_obj = Phone.from_dict(up)
        elif "cpu" in up:
            product_obj = Laptop.from_dict(up)
        elif "sensor_type" in up:
            product_obj = Camera.from_dict(up)
        print(product_obj, end="\n---------------------\n")


def approve_product_or_seller(product_or_seller):
    while True:
        try:
            if product_or_seller == "product":
                show_unapproved_products()

            print(colorama.Fore.WHITE)
            product_or_seller_id = int(
                input(f"Enter {product_or_seller} ID to approve:\n")
            )
            if product_or_seller == "seller":
                approved = SellerEmployee.approve_seller(product_or_seller_id)
            elif product_or_seller == "product":
                approved = SellerEmployee.approve_product(product_or_seller_id)

            if approved:
                print_successful(f"{product_or_seller} was approved successfuly!\n")
                again = input("Approve another?\n1- Yes\n")
                if again != "1":
                    break
        except ValueError as e:
            print_error(e)


def remove_seller_or_product(product_or_seller):
    while True:
        try:
            product_or_seller_id = input(
                f"Enter {product_or_seller} ID to remove (Enter 'e' to exit):\n"
            )
            if product_or_seller_id.lower() == "e":
                print_successful(f"Exited removing {product_or_seller}!\n")
                break

            if not product_or_seller_id.isdigit():
                print_error("ID must be a number.\n")
                continue

            product_or_seller_id = int(product_or_seller_id)

            if product_or_seller == "seller":
                removed = SellerEmployee.remove_seller(product_or_seller_id)
            elif product_or_seller == "product":
                removed = SellerEmployee.remove_product(product_or_seller_id)

            if removed:
                print_successful(f"{product_or_seller} was removed successfuly!\n")
                again = input("Remove another?\n1- Yes\n")
                if again != "1":
                    break
        except ValueError as e:
            print_error(e)


def show_all_products():
    phones = Phone.get_approved_products()
    laptops = Laptop.get_approved_products()
    cameras = Camera.get_approved_products()
    print(colorama.Fore.BLUE)
    print("\n======= All products =======\n")
    for phone in phones:
        print(Phone.from_dict(phone), end="\n--------------------\n")
    for laptop in laptops:
        print(Laptop.from_dict(laptop), end="\n--------------------\n")
    for camera in cameras:
        print(Camera.from_dict(camera), end="\n--------------------\n")


@staticmethod
def filter_products():

    products = (
        Phone.get_approved_products()
        + Laptop.get_approved_products()
        + Camera.get_approved_products()
    )

    while True:
        try:
            print(
                "\nFilter By:\n"
                "1- Name\n"
                "2- Brand\n"
                "3- Category\n"
                "4- Price\n"
                "5- Exit"
            )

            choice = input("Please choose:\n")

            match choice:
                case "1":
                    name = input("Enter product name:\n")

                    filtered_products = list(
                        filter(
                            lambda product: name.lower() in product["name"].lower(),
                            products,
                        )
                    )

                case "2":
                    brand = input("Enter brand:\n")

                    filtered_products = list(
                        filter(
                            lambda product: brand.lower() in product["brand"].lower(),
                            products,
                        )
                    )

                case "3":
                    category = input("Enter category:\n")

                    filtered_products = list(
                        filter(
                            lambda product: category.lower()
                            == product["category"].lower(),
                            products,
                        )
                    )

                case "4":
                    min_price = int(input("Enter minimum price:\n"))
                    max_price = int(input("Enter maximum price:\n"))

                    filtered_products = list(
                        filter(
                            lambda product: min_price <= product["price"] <= max_price,
                            products,
                        )
                    )

                case "5":
                    break

                case _:
                    raise ValueError("Please only choose from options.\n")

            if not filtered_products:
                print_error("\nNo products found.\n")
                continue

            for product in filtered_products:
                print(colorama.Fore.BLUE)
                if "battery_mah" in product:
                    product_obj = Phone.from_dict(product)
                elif "cpu" in product:
                    product_obj = Laptop.from_dict(product)
                elif "sensor_type" in product:
                    product_obj = Camera.from_dict(product)
                print(product_obj, end="\n-------------------------\n")
                print(colorama.Fore.WHITE)

        except ValueError as e:
            print_error(e)


import csv


@staticmethod
def export_customer_or_seller(employee_type):

    data = {
        "customer": {"file": CustomerEmployee.get_customers, "name": "Customers"},
        "seller": {"file": SellerEmployee.get_sellers, "name": "Sellers"},
    }

    if employee_type not in data:
        raise ValueError("Invalid employee type.")

    user_data = data[employee_type]

    users = user_data["file"]()

    if not users:
        raise ValueError(f"No {employee_type}s found.")

    while True:
        try:
            print("\nExport As:\n" "1- CSV\n" "2- TXT\n" "3- Exit")

            choice = input("Please choose:\n")

            if choice == "1":

                filename = f"./Reports/{user_data['name']}.csv"

                fieldnames = users[0].keys()

                with open(filename, "w", newline="", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)

                    writer.writeheader()
                    writer.writerows(users)

                print_successful(f"{user_data['name']} exported successfully to CSV.")

                return True

            elif choice == "2":

                filename = f"./Reports/{user_data['name']}.txt"

                with open(filename, "w", encoding="utf-8") as file:

                    for user in users:

                        for key, value in user.items():
                            file.write(f"{key}: {value}\n")

                        file.write("\n")

                print_successful(f"{user_data['name']} exported successfully to TXT.")

                return True

            elif choice == "3":
                return False

            else:
                print_error("Please only choose from options.")

        except ValueError as e:
            print_error(e)


# Panels -----------------------------------------------------------------


def customers_panel(customer):
    while True:

        print_successful(
            f"Welcome Customer {customer.firstname} {customer.lastname}!\n"
        )

        show_customer_menu()
        choice = input("Please Choose:\n")

        match choice:
            case "1":
                customers_Shop_panel(customer)
            case "2":
                user_Ticket_panel(customer, "customer")
            case "3":
                print_account_info(customer)
            case "4":
                break
            case _:
                print_error("Please only choose from options")


def customers_Shop_panel(customer):
    while True:
        print_successful(
            f"Welcome Customer {customer.firstname} {customer.lastname}!\n"
        )

        show_products()

        show_customer_shop_menu()
        choice = input("Please Choose:\n")

        match choice:
            case "1":
                try:
                    customer.checkout()
                except ValueError as e:
                    print_error(e)
            case "2":
                filter_products()
            case "3":
                handle_customer_add_actions(customer, "cart")
            case "4":
                handle_customer_add_actions(customer, "favorites")
            case "5":
                add_cart_to_favorites(customer)
            case "6":
                handle_customer_remove_actions(customer, "cart")
            case "7":
                handle_customer_remove_actions(customer, "favorites")
            case "8":
                show_customer_cart_and_favorites(customer.id)
            case "9":
                add_to_balance(customer)
            case "10":
                break
            case _:
                print_error("Please only choose from options")


def user_Ticket_panel(user, submit_type):
    while True:
        print_successful(f"Welcome {submit_type} {user.firstname} {user.lastname}!\n")
        show_ticket_menu()
        choice = input("Please Choose:\n")

        match choice:
            case "1":
                submit_ticket(user, submit_type)
            case "2":
                see_user_tickets(user, submit_type)
            case "3":
                break
            case _:
                print_error("Please only choose from options")


def sellers_panel(seller):
    while True:
        print_successful(f"Welcome seller {seller.firstname} {seller.lastname}!\n")

        show_seller_menu()
        choice = input("Please Choose:\n")

        match choice:
            case "1":
                sellers_product_panel(seller)
            case "2":
                user_Ticket_panel(seller, "seller")
            case "3":
                print_account_info(seller)
            case "4":
                break
            case _:
                print_error("Please only choose from options")


def sellers_product_panel(seller):

    while True:
        print_successful(f"Welcome Seller {seller.firstname} {seller.lastname}!\n")

        show_seller_product_menu()
        choice = input("Please Choose:\n")
        match choice:
            case "1":
                make_product(seller)
                pass
            case "2":
                see_seller_selling_products(seller)
                pass
            case "3":
                see_seller_unapproved_products(seller)
                pass
            case "4":
                delete_product_from_seller(seller)
                pass
            case "5":
                edit_product(seller)
                pass
            case "6":
                break
            case _:
                print_error("Please only choose from options")


def customer_employee_panel(customer_employee):
    while True:
        print_successful(
            f"Welcome customer employee {customer_employee.firstname} {customer_employee.lastname}!"
        )

        show_customer_employee_menu()
        choice = input("Please Choose:\n")
        match choice:
            case "1":
                employee_Ticket_panel(
                    customer_employee, "customer_employee", "customer"
                )
                pass
            case "2":
                remove_customer()
            case "3":
                print_account_info(customer_employee)
            case "4":
                break
            case _:
                print_error("Please only choose from options")


def seller_employee_panel(seller_employee):
    while True:
        print_successful(
            f"Welcome seller employee {seller_employee.firstname} {seller_employee.lastname}!"
        )

        show_seller_employee_menu()
        choice = input("Please Choose:\n")
        match choice:
            case "1":
                seller_employee_seller_panel(seller_employee)
            case "2":
                seller_employee_product_panel(seller_employee)
            case "3":
                employee_Ticket_panel(seller_employee, "seller_employee", "seller")
            case "4":
                print_account_info(seller_employee)
            case "5":
                break
            case _:
                print_error("Please only choose from options")


def seller_employee_seller_panel(seller_employee):
    while True:
        print_successful(
            f"Welcome seller employee {seller_employee.firstname} {seller_employee.lastname}!"
        )
        show_unapproved_sellers()
        show_seller_employee_seller_menu()
        choice = input("Please Choose:\n")
        match choice:
            # "1- Approve seller\n" "2- Remove seller\n" "3- Back\n",
            case "1":
                approve_product_or_seller("seller")
            case "2":
                remove_seller_or_product("seller")
            case "3":
                break
            case _:
                print_error("Please only choose from options")


def seller_employee_product_panel(seller_employee):
    while True:
        print_successful(
            f"Welcome seller employee {seller_employee.firstname} {seller_employee.lastname}!"
        )

        show_all_products()
        show_seller_employee_product_menu()
        choice = input("Please Choose:\n")
        match choice:
            # "1- Approve product\n" "2- Remove product\n" "3- Edit product\n" "4- Back\n",
            case "1":
                approve_product_or_seller("product")
            case "2":
                remove_seller_or_product("product")
            case "3":
                edit_product()
            case "4":
                break
            case _:
                print_error("Please only choose from options")


def show_employee_manager_panel(manager, employee_type):
    while True:
        print_successful(
            f"Welcome {employee_type.capitalize()} Manager {manager.firstname} {manager.lastname}!\n"
        )

        if employee_type == "customer":
            show_customer_employee_manager_menu()
        else:
            show_seller_employee_manager_menu()

        choice = input("Please Choose:\n")

        match choice:

            case "1":
                hire_employee(employee_type)
            case "2":
                fire_employee(employee_type)

            case "3":
                give_employee_raise(employee_type)

            case "4":
                show_all_employees(employee_type)

            case "5":
                show_all_users(employee_type)

            case "6":
                generate_top3_report(employee_type)

            case "7":
                export_customer_or_seller(employee_type)

            case "8":
                show_manager_account_info(manager)

            case "9":
                break

            case _:
                print_error("Please only choose from options")


def employee_Ticket_panel(user, employee_type, sender_type):
    while True:
        role = employee_type.split("_")
        print_successful(
            f"Welcome {role[0]} {role[1]} {user.firstname} {user.lastname}!\n"
        )
        show_user_tickets("unanswered", sender_type)
        show_employee_Ticket_menu()
        choice = input("Please Choose:\n")

        match choice:
            case "1":
                answer_ticket(employee_type)
            case "2":
                show_user_tickets("all", sender_type)
            case "3":
                break
            case _:
                print_error("Please only choose from options")


# Main -----------------------------------------------------------------------


def main():

    customersManager = CustomerManager()
    customersManager.firstname = "Radin"
    customersManager.lastname = "Motahhary"
    customersManager.username = "radinm123"
    customersManager.password = "Radinian@123"
    customersManager.age = "21"
    customersManager.phone_num = "9379499511"
    customersManager.address = "Karaj_ mehrshahr"

    sellersManager = SellerManager()
    sellersManager.firstname = "Radin"
    sellersManager.lastname = "Motahhary"
    sellersManager.username = "radinm123"
    sellersManager.password = "Radinian@123"
    sellersManager.age = "21"
    sellersManager.phone_num = "9379499511"
    sellersManager.address = "Karaj_ mehrshahr"

    managers = {"customer": customersManager, "seller": sellersManager}

    user_types = {
        "1": "customer",
        "2": "seller",
        "3": "customer_employee",
        "4": "seller_employee",
        "5": "customer_manager",
        "6": "seller_manager",
    }

    while True:

        show_main_menu()

        choice = input("Please choose:\n")

        if choice in user_types:

            username = input("Please enter your username:\n")
            password = input("Please enter your password:\n")

            login_user(username, password, user_types[choice], managers)

        elif choice == "7":

            print_error("\nBye!\n")
            break

        else:
            print_error("Please only choose from options")


if __name__ == "__main__":
    main()
