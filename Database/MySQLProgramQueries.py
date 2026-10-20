from Database.MySQLCommands import MySQLcommands


class MySQLProgramQueries:

    # User Query //////////////////////////

    @staticmethod
    def check_login_query(username, password, role):

        allowed_tables = {
            "customer": "customers",
            "seller": "sellers",
            "employee": "employees",
        }

        table = allowed_tables.get(role)

        if table is None:
            raise ValueError("Invalid role")

        query = f"""
            SELECT *
            FROM {table}
            LIMIT 1
        """
        
        cursor = MySQLcommands.execute_query(query, commit=False)
        
        try:
            has_users = cursor.fetchone() is not None   
        finally:
            cursor.close()
        
        query = f"""
            SELECT *
            FROM {table}
            WHERE username = %s
                AND password = %s
                
            LIMIT 1
        """

        cursor = MySQLcommands.execute_query(query, (username, password))

        try:
            return cursor.fetchone(), has_users
        finally:
            cursor.close()

    # Seller queries /////////////////////////////

    @staticmethod
    def add_seller_query(
        firstname, lastname, username, password, age, phone_num, address, balance
    ):
        query = """
        INSERT INTO sellers (
            firstname, lastname, username, password,
            age, phone_num, address, balance
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        params = (
            firstname,
            lastname,
            username,
            password,
            age,
            phone_num,
            address,
            balance,
        )

        cursor = MySQLcommands.execute_query(query, params)

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def get_sellers_query(status):
        query = """
            SELECT * from sellers
            WHERE status = %s
        """

        cursor = MySQLcommands.execute_query(query, (status,))

        try:
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def get_approved_seller_query(seller_id):
        query = """
            SELECT * from sellers
            WHERE id = %s
                AND status = %s
        """
        cursor = MySQLcommands.execute_query(query, (seller_id, "approved"))

        try:
            return cursor.fetchone()
        finally:
            cursor.close()

    @staticmethod
    def approve_seller_query(seller_id):
        query = """
            UPDATE sellers
            SET status = "approved"
            WHERE id = %s 
                AND status = "pending"
        """

        cursor = MySQLcommands.execute_query(query, (seller_id,))

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def delete_seller_query(seller_id):
        query = """
            DELETE FROM sellers
            WHERE id = %s 
                AND status = "approved"
        """

        cursor = MySQLcommands.execute_query(query, (seller_id,))

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def get_Seller_pending_products_query(seller_id):
        query = """
            SELECT
                p.*,

                c.resolution_mp,
                c.zoom_factor,
                c.sensor_type,

                l.ram_gb AS laptop_ram_gb,
                l.storage_gb AS laptop_storage_gb,
                l.cpu,

                ph.ram_gb AS phone_ram_gb,
                ph.storage_gb AS phone_storage_gb,
                ph.battery_mah

            FROM products AS p

            LEFT JOIN cameras AS c
                ON p.id = c.product_id

            LEFT JOIN laptops AS l
                ON p.id = l.product_id

            LEFT JOIN phones AS ph
                ON p.id = ph.product_id

            WHERE p.status = 'pending' AND p.seller_id = %s; 
        """

        cursor = MySQLcommands.execute_query(query, (seller_id,))
        try:
            pending_products = cursor.fetchall()
            return pending_products
        finally:
            cursor.close()

    @staticmethod
    def delete_seller_product_query(product_id, seller_id):
        query = """
            DELETE FROM PRODUCTS
            WHERE id = %s
                AND seller_id = %s;
        """

        cursor = MySQLcommands.execute_query(query, (product_id, seller_id))

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    # Customer queries /////////////////////////////

    @staticmethod
    def get_customers_query():
        query = """
            SELECT * FROM customers
        """

        cursor = MySQLcommands.execute_query(query)

        try:
            customers = cursor.fetchall()
            return customers
        finally:
            cursor.close()

    @staticmethod
    def delete_customer_query(customer_id):
        query = """
            DELETE FROM customers
            WHERE id = %s
        """

        cursor = MySQLcommands.execute_query(query, (customer_id,))

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def add_customer_query(
        firstname, lastname, username, password, age, phone_num, address, balance
    ):
        query = """
        INSERT INTO customers (
            firstname, lastname, username, password,
            age, phone_num, address, balance
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        params = (
            firstname,
            lastname,
            username,
            password,
            age,
            phone_num,
            address,
            balance,
        )

        cursor = MySQLcommands.execute_query(query, params)

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def set_customer_balance_query(amount, customer_id):
        query = """
            UPDATE customers
            SET balance = %s
            WHERE id = %s
        """

        cursor = MySQLcommands.execute_query(query, (amount, customer_id))

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def get_customer_balance_query(customer_id):
        query = """
            SELECT balance
            FROM customers
            WHERE id = %s
        """

        cursor = MySQLcommands.execute_query(query, (customer_id,))

        try:
            result = cursor.fetchone()
            return result["balance"] if result else None
        finally:
            cursor.close()
            
            
    # Cart Item queries /////////////////////////////

    @staticmethod
    def add_cart_item_query(customer_id, product_id):
        query = """
            INSERT INTO cart_items (customer_id, product_id)
            VALUES (%s, %s)
        """

        cursor = MySQLcommands.execute_query(query, (customer_id, product_id))
        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def add_many_cart_item_query(items):
        query = """
            INSERT INTO cart_items (customer_id, product_id)
            VALUES (%s, %s)
        """

        cursor = MySQLcommands.execute_many_queries(query, items)

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()
            
            
    @staticmethod
    def get_customer_cart_total_price_query(customer_id):
        query = """
            SELECT COALESCE(SUM(p.price), 0) AS total_price
            FROM cart_items AS ci
            JOIN products AS p
                ON ci.product_id = p.id
            WHERE ci.customer_id = %s
        """

        cursor = MySQLcommands.execute_query(query, (customer_id,))

        try:
            result = cursor.fetchone()
            return result["total_price"]
        finally:
            cursor.close()


    @staticmethod
    def delete_cart_item_query(cart_item_id, customer_id):
        query = """
            DELETE FROM cart_items
            WHERE id = %s
                AND customer_id = %s
        """

        cursor = MySQLcommands.execute_query(query, (cart_item_id, customer_id))

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def delete_all_customer_cart_items_query(customer_id):
        query = """
            DELETE FROM cart_items
            WHERE customer_id = %s
        """

        cursor = MySQLcommands.execute_query(query, (customer_id,))
        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def get_customer_cart_items_query(customer_id):
        query = """
            SELECT * FROM cart_items
            WHERE customer_id = %s
        """

        cursor = MySQLcommands.execute_query(query, (customer_id,))

        try:
            cart_items = cursor.fetchall()
            return cart_items
        finally:
            cursor.close()

    @staticmethod
    def add_cart_items_to_sales_query(cart_items):
        query = """
            INSERT INTO sales (customer_id, product_id)
            Values (%s, %s)
        """

        cursor = MySQLcommands.execute_many_queries(query, cart_items)
        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()
            

    @staticmethod
    def add_cart_total_to_sellers_balance_query(customer_id):
        query = """
            UPDATE sellers AS s
            JOIN (
                SELECT
                    p.seller_id,
                    SUM(p.price) AS total_amount
                FROM cart_items AS ci
                JOIN products AS p
                    ON ci.product_id = p.id
                WHERE ci.customer_id = %s
                GROUP BY p.seller_id
            ) AS seller_totals
                ON s.id = seller_totals.seller_id
            SET s.balance = s.balance + seller_totals.total_amount
        """

        cursor = MySQLcommands.execute_query(query, (customer_id,))

        try:
            return cursor.rowcount
        finally:
            cursor.close()
        
        
    # Favorites queries /////////////////////////////

    @staticmethod
    def add_customer_favorites_query(customer_id, product_id):
        query = """
            INSERT INTO favorites (customer_id, product_id)
            VALUES (%s, %s)
        """

        cursor = MySQLcommands.execute_query(query, (customer_id, product_id))
        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def delete_customer_favorite_query(favorite_id, customer_id):
        query = """
            DELETE FROM favorites
            WHERE id = %s
                AND customer_id = %s
        """

        cursor = MySQLcommands.execute_query(query, (favorite_id, customer_id))
        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def get_customer_favorites_query(customer_id):
        query = """
            SELECT * FROM favorites
            WHERE customer_id = %s
        """

        cursor = MySQLcommands.execute_query(query, (customer_id,))

        try:
            favorites = cursor.fetchall()
            return favorites
        finally:
            cursor.close()

    @staticmethod
    def delete_all_customer_favorites_query(customer_id):
        query = """
            DELETE FROM favorites
            WHERE customer_id = %s
        """

        cursor = MySQLcommands.execute_query(query, (customer_id,))
        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    # Tickets queries /////////////////////////////////

    @staticmethod
    def add_ticket_query(from_name, from_id, sender_type, request):
        query = """
            INSERT INTO tickets (from_name, from_id, sender_type, request)
            VALUES (%s, %s, %s, %s)
        """

        cursor = MySQLcommands.execute_query(
            query, (from_name, from_id, sender_type, request)
        )

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    @staticmethod
    def get_user_tickets_query(sender_type, from_id):
        allowed_types = {"customer", "seller"}

        if sender_type not in allowed_types:
            raise ValueError("Invalid sender type")

        query = """
            SELECT *
            FROM tickets
            WHERE sender_type = %s
            AND from_id = %s
        """

        cursor = MySQLcommands.execute_query(query, (sender_type, from_id))

        try:
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def answer_ticket_query(ticket_id, answer):
        query = """
            UPDATE tickets
            Set response = %s
            WHERE id = %s 
                AND response = ''
        """

        cursor = MySQLcommands.execute_query(query, (answer, ticket_id))

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    # Product Queries ////////////////////////////

    @staticmethod
    def add_product_query(
        seller_id,
        name,
        brand,
        price,
        category,
        child_field1,
        child_field2,
        child_field3,
    ):
        database_fields = {
            "laptop": ("laptops", ("ram_gb", "storage_gb", "cpu")),
            "camera": ("cameras", ("resolution_mp", "zoom_factor", "sensor_type")),
            "phone": ("phones", ("ram_gb", "storage_gb", "battery_mah")),
        }

        if category not in database_fields:
            raise ValueError("Invalid product category")

        table, fields = database_fields[category]

        connection = MySQLcommands.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(
                """
                INSERT INTO products
                    (seller_id, name, brand, price, category, status)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (seller_id, name, brand, price, category, "pending"),
            )

            product_id = cursor.lastrowid

            query = f"""
                INSERT INTO {table}
                    (product_id, {fields[0]}, {fields[1]}, {fields[2]})
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (product_id, child_field1, child_field2, child_field3),
            )

            connection.commit()
            return True

        except Exception:
            connection.rollback()
            raise

        finally:
            cursor.close()

    @staticmethod
    def delete_product_query(product_id):
        query = """
            DELETE FROM products
            WHERE id = %s 
                AND status = "approved"
        """

        cursor = MySQLcommands.execute_query(query, (product_id,))

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()


    @staticmethod
    def edit_product_query(
        product_id,
        name,
        brand,
        price,
        child_field1,
        child_field2,
        child_field3,
    ):
        database_fields = {
            "laptop": ("laptops", ("ram_gb", "storage_gb", "cpu")),
            "camera": ("cameras", ("resolution_mp", "zoom_factor", "sensor_type")),
            "phone": ("phones", ("ram_gb", "storage_gb", "battery_mah")),
        }

        connection = MySQLcommands.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT category FROM products WHERE id = %s",
                (product_id,),
            )

            product = cursor.fetchone()

            if product is None:
                return False

            table, fields = database_fields[product["category"]]

            cursor.execute(
                """
                UPDATE products
                SET name = %s, brand = %s, price = %s
                WHERE id = %s
                """,
                (name, brand, price, product_id),
            )

            query = f"""
                UPDATE {table}
                SET {fields[0]} = %s,
                    {fields[1]} = %s,
                    {fields[2]} = %s
                WHERE product_id = %s
            """

            cursor.execute(
                query,
                (child_field1, child_field2, child_field3, product_id),
            )

            connection.commit()
            return True

        except Exception:
            connection.rollback()
            raise

        finally:
            cursor.close()

    @staticmethod
    def get_products_query(status):
        product_status = ("pending", "approved")

        if status not in product_status:
            raise ValueError("status is invalid.")

        query = """
            SELECT * from products
            WHERE status = %s
        """

        cursor = MySQLcommands.execute_query(query, (status,))

        try:
            return cursor.fetchall()
        finally:
            cursor.close()

    @staticmethod
    def approve_product_query(product_id):
        query = """
            UPDATE products
            SET status = "approved"
            WHERE id = %s 
                AND status = "pending"
        """

        cursor = MySQLcommands.execute_query(query, (product_id,))

        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()

    # Customer manager queries/////////////////////////

    @staticmethod
    def add_employee_query(
        firstname,
        lastname,
        username,
        password,
        age,
        phone_num,
        address,
        bank_account_num,
        salary,
        role,
    ):
        query = """
            INSERT INTO employees (
                firstname, lastname, username, password,
                age, phone_num, address, bank_account_num, salary, role
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor = MySQLcommands.execute_query(
            query,
            (
                firstname,
                lastname,
                username,
                password,
                age,
                phone_num,
                address,
                bank_account_num,
                salary,
                role,
            ),
        )

        try:
            return cursor.rowcount
        finally:
            cursor.close()

    @staticmethod
    def delete_employee_query(employee_id, role):

        query = """
            DELETE FROM employees
            WHERE id = %s
                AND role = %s
        """

        cursor = MySQLcommands.execute_query(query, (employee_id, role))

        try:
            return cursor.rowcount
        finally:
            cursor.close()

    @staticmethod
    def get_employee_query(employee_id, role):

        query = """
            SELECT * FROM employees
            WHERE id = %s
                AND role = %s
        """

        cursor = MySQLcommands.execute_query(query, (employee_id, role))

        try:
            return cursor.fetchone()
        finally:
            cursor.close()
