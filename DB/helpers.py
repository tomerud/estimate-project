import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def check_destination_exists(destination):
    """
    Checks if the destination exists in the `cities` table.
    Returns True if it exists, otherwise False.
    """
    try:
        # Connect to the MySQL database using environment variables
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
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