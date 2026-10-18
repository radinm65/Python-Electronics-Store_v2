import mysql.connector


class MySQLcommands:
    _connection = None

    @staticmethod
    def connect_to_mysql():
        if (
            MySQLcommands._connection is None
            or MySQLcommands._connection.is_connected() == False
        ):
            MySQLcommands._connection = mysql.connector.connect(
                host="localhost", user="root", port=3306
            )
        return MySQLcommands._connection

    @staticmethod
    def initialize_database():
        cursor = MySQLcommands._connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS electronic_store")
        cursor.execute("USE electronic_store")

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                firstname VARCHAR(20) NOT NULL,
                lastname VARCHAR(20) NOT NULL,
                username VARCHAR(20) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                phone_num VARCHAR(10) NOT NULL,
                address VARCHAR(50) NOT NULL,
                balance INT NOT NULL
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sellers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                firstname VARCHAR(20) NOT NULL,
                lastname VARCHAR(20) NOT NULL,
                username VARCHAR(20) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                phone_num VARCHAR(10) NOT NULL,
                address VARCHAR(50) NOT NULL,
                balance INT NOT NULL,

                status ENUM('pending', 'approved')
                        NOT NULL DEFAULT 'pending'
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                seller_id INT NOT NULL,
                name VARCHAR(100) NOT NULL,
                brand VARCHAR(50) NOT NULL,
                price INT NOT NULL,
                
                category ENUM('camera', 'laptop', 'phone')
                    NOT NULL,
                
                status ENUM('pending', 'approved')
                    NOT NULL DEFAULT 'pending',
                    
                date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                
                FOREIGN KEY (seller_id)
                    REFERENCES sellers(id)
                    ON DELETE CASCADE
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS cameras (
                product_id INT PRIMARY KEY,
                resolution_mp INT NOT NULL,
                zoom_factor INT NOT NULL,
                sensor_type VARCHAR(15) NOT NULL,
                
                FOREIGN KEY (product_id)
                    REFERENCES products(id)
                    ON DELETE CASCADE
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS laptops (
                product_id INT PRIMARY KEY,
                ram_gb INT NOT NULL,
                storage_gb INT NOT NULL,
                cpu VARCHAR(30) NOT NULL,
                
                FOREIGN KEY (product_id)
                    REFERENCES products(id)
                    ON DELETE CASCADE
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS phones (
                product_id INT PRIMARY KEY,
                ram_gb INT NOT NULL,
                storage_gb INT NOT NULL,
                battery_mah INT NOT NULL,
                
                FOREIGN KEY (product_id)
                    REFERENCES products(id)
                    ON DELETE CASCADE
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS cart_items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT NOT NULL,
                product_id INT NOT NULL,
                
                FOREIGN KEY (customer_id)  
                    REFERENCES customers(id),
                    
                FOREIGN KEY ( product_id)  
                    REFERENCES products(id),
                    
                UNIQUE (customer_id, product_id)
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS favorites (
                id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT NOT NULL,
                product_id INT NOT NULL,
                
                FOREIGN KEY (customer_id)  
                    REFERENCES customers(id),
                    
                FOREIGN KEY (product_id)  
                    REFERENCES products(id),
                    
                UNIQUE (customer_id, product_id)
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sales (
                id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT NOT NULL,
                product_id INT NOT NULL,
                sale_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (customer_id)
                    REFERENCES customers(id),

                FOREIGN KEY (product_id)
                    REFERENCES products(id)
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                firstname VARCHAR(20) NOT NULL,
                lastname VARCHAR(20) NOT NULL,
                username VARCHAR(20) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                phone_num VARCHAR(10) NOT NULL,
                address VARCHAR(50) NOT NULL,
                bank_account_num VARCHAR(16) NOT NULL,
                salary INT NOT NULL,
                role ENUM('customer_support', 'seller_manager') NOT NULL,
                date_hired TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tickets (
                id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT NULL,
                seller_id INT NULL,
                request TEXT NOT NULL,
                response TEXT NOT NULL DEFAULT '',
                date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

                FOREIGN KEY (customer_id) REFERENCES customers(id),
                FOREIGN KEY (seller_id) REFERENCES sellers(id),

                CHECK (
                    (customer_id IS NULL AND seller_id IS NOT NULL)
                    OR
                    (customer_id IS NOT NULL AND seller_id IS NULL)
                )
            )
        """
        )

        MySQLcommands._connection.commit()

    @staticmethod
    def execute_query(query, params=None):
        cursor = MySQLcommands._connection.cursor(dictionary=True)

        try:
            cursor.execute(query, params)
            MySQLcommands._connection.commit()
            return cursor

        except mysql.connector.Error:
            MySQLcommands._connection.rollback()
            cursor.close()
            raise 
        
    @staticmethod
    def execute_many_queries(query, data_list):
        cursor = MySQLcommands._connection.cursor(dictionary=True)

        try:
            cursor.executemany(query, data_list)
            MySQLcommands._connection.commit()
            return cursor

        except mysql.connector.Error:
            MySQLcommands._connection.rollback()
            cursor.close()
            raise 

    @staticmethod
    def close_connection():
        if (
            MySQLcommands._connection is not None
            and MySQLcommands._connection.is_connected()
        ):
            MySQLcommands._connection.close()
            MySQLcommands._connection = None
