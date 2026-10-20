import mysql.connector


class MySQLcommands:
    _connection = None

    @staticmethod
    def connect_to_mysql():
        if (
            MySQLcommands._connection is None
            or not MySQLcommands._connection.is_connected()
        ):
            MySQLcommands._connection = mysql.connector.connect(
                host="localhost", user="root", port=3306
            )
        return MySQLcommands._connection

    @staticmethod
    def initialize_database():
        
        connection = MySQLcommands.connect_to_mysql()
        cursor = connection.cursor()
        
        try:
        
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
                        REFERENCES customers(id)
                        ON DELETE CASCADE,
                        
                    FOREIGN KEY ( product_id)  
                        REFERENCES products(id)
                        ON DELETE CASCADE,
                        
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
                        REFERENCES customers(id)
                        ON DELETE CASCADE,
                        
                    FOREIGN KEY (product_id)  
                        REFERENCES products(id)
                        ON DELETE CASCADE,
                        
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
                    role ENUM('customer_employee', 'seller_employee') NOT NULL,
                    date_hired TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tickets (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    from_name VARCHAR(20) NOT NULL,
                    from_id INT NOT NULL,
                    sender_type ENUM('customer', 'seller') NOT NULL,
                    request TEXT NOT NULL,
                    response TEXT NOT NULL DEFAULT (''),
                    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    
                    INDEX idx_sender (sender_type, from_id)
                );
            """
            )

            connection.commit()
            
        finally:
            cursor.close()
            

    @staticmethod
    def execute_query(query, params=None, commit=True):
        connection = MySQLcommands.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(query, params)

            if commit:
                connection.commit()

            return cursor

        except mysql.connector.Error as e:
            connection.rollback()
            cursor.close()

            if e.errno == 1062:
                if "username" in e.msg:
                    raise ValueError("Username already exists.")
                raise ValueError("This record already exists.")

            if e.errno == 1451:
                raise ValueError(
                    "This record can't be removed because it is linked to sales."
                )

            raise
        
    @staticmethod
    def execute_many_queries(query, data_list, commit=True):
        connection = MySQLcommands.connect_to_mysql()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.executemany(query, data_list)

            if commit:
                connection.commit()

            return cursor

        except mysql.connector.Error:
            connection.rollback()
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
