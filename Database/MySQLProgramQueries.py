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
        last_id = cursor.lastrowid
        cursor.close()
        return last_id
    
    
    
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
            unapproved_products = cursor.fetchall()
            return unapproved_products
        finally:
            cursor.close()
            
            
            
    def delete_seller_product_query(product_id):
        query = """
            DELETE FROM PRODUCTS
            WHERE id = %s
        """
        
        cursor = MySQLcommands.execute_query(query, (product_id,))
        deleted = cursor.rowcount > 0
        cursor.close()
        
        return deleted
    
    
        
            
            
    
        
