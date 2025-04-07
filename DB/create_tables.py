import mysql.connector
from mysql.connector import Error

def create_tables():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="127.0.0.1",  # Hostname
            user="root",       # Username
            password="112145",       # Password (leave empty if not set)
            database="estimate"  # Database name
        )

        if connection.is_connected():
            print("Connected to the database")

            # Create a cursor object
            cursor = connection.cursor()

            # SQL to create the `countries` table
            create_countries_table = """
            CREATE TABLE IF NOT EXISTS countries (
                country_id INT AUTO_INCREMENT PRIMARY KEY,
                country_name VARCHAR(255) NOT NULL,
                hdi DECIMAL(5, 3) NOT NULL
            );
            """

            # SQL to create the `cities` table
            create_cities_table = """
            CREATE TABLE IF NOT EXISTS cities (
                city_id INT AUTO_INCREMENT PRIMARY KEY,
                city_name VARCHAR(255) NOT NULL,
                country_id INT NOT NULL,
                longitude DECIMAL(10, 7) NOT NULL,
                latitude DECIMAL(10, 7) NOT NULL,
                FOREIGN KEY (country_id) REFERENCES countries(country_id)
            );
            """

            # Execute the SQL commands
            cursor.execute(create_countries_table)
            print("Table `countries` created successfully (if not exists).")

            cursor.execute(create_cities_table)
            print("Table `cities` created successfully (if not exists).")

            # Commit the changes
            connection.commit()

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_tables()