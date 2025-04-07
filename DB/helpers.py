import mysql.connector
from mysql.connector import Error

def check_destination_exists(destination):
    """
    Checks if the destination exists in the `cities` table.
    Returns True if it exists, otherwise False.
    """
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="127.0.0.1",  # Hostname
            user="root",       # Username
            password="112145", # Password
            database="estimate"  # Database name
        )

        if connection.is_connected():
            print("Connected to the database")

            # Create a cursor object
            cursor = connection.cursor()

            # Query to check if the destination exists
            check_destination_query = """
            SELECT COUNT(*) FROM cities WHERE city_name = %s;
            """
            cursor.execute(check_destination_query, (destination,))
            result = cursor.fetchone()

            # Return True if the destination exists, otherwise False
            return result[0] > 0

    except Error as e:
        print(f"Error: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")