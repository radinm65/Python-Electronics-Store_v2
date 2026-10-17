import mysql.connector


class mysqlcommands:
    _connection = None

    @staticmethod
    def connect_to_mysql():
        if (
            mysqlcommands._connection is None
            or mysqlcommands._connection.is_connected() == False
        ):
            mysqlcommands._connection = mysql.connector.connect(
                host="localhost", user="root", port=3306
            )
        return mysqlcommands._connection

    @staticmethod
    def initialize_database():
        cursor = mysqlcommands._connection.cursor()
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

        mysqlcommands._connection.commit()

    @staticmethod
    def execute_query(query, params=None):
        cursor = mysqlcommands._connection.cursor()
        cursor.execute(query, params)
        mysqlcommands._connection.commit()
        return cursor

    @staticmethod
    def close_connection():
        if (
            mysqlcommands._connection is not None
            and mysqlcommands._connection.is_connected()
        ):
            mysqlcommands._connection.close()
            mysqlcommands._connection = None
