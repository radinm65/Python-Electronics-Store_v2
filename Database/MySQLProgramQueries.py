from Database.MySQLCommands import MySQLcommands


class MySQLProgramQueries:
    
    # Seller queries /////////////////////////////
    
    @staticmethod
    def save_seller_query(
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
    def get_pending_products_query(seller_id):
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
    def save_customer_query(
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
    def remove_customer_cart_item_query(cart_item_id, customer_id):
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
    def remove_all_customer_cart_items_query(customer_id):
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
    def get_customer_cart_items(customer_id):
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
    def remove_customer_favorite_query(favorite_id, customer_id):
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
    def get_customer_favorites(customer_id):
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
    def remove_all_customer_favorites_query(customer_id):
        query = """
            DELETE FROM favorites
            WHERE customer_id = %s
        """
                
        cursor = MySQLcommands.execute_query(query, (customer_id,))
        try:
            return cursor.rowcount > 0
        finally:
            cursor.close()
            
    

    
        
        
        
        
        
        
    
        
    
    
        
            
            
    
        
