import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_tables_info():
    """
    Retrieves and prints information about the tables in the database.
    Includes table names, column names, data types, keys, and other metadata.
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

            # Query to get metadata from INFORMATION_SCHEMA
            metadata_query = """
            SELECT 
                TABLE_NAME AS table_name,
                COLUMN_NAME AS column_name,
                DATA_TYPE AS data_type,
                IS_NULLABLE AS is_nullable,
                COLUMN_KEY AS column_key,
                EXTRA AS extra
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = %s
            ORDER BY TABLE_NAME, ORDINAL_POSITION;
            """
            cursor.execute(metadata_query, (os.getenv("DB_NAME"),))
            metadata = cursor.fetchall()

            # Print the metadata
            print(f"{'Table Name':<20} {'Column Name':<20} {'Data Type':<15} {'Is Nullable':<15} {'Column Key':<15} {'Extra':<15}")
            print("-" * 100)
            for row in metadata:
                print(f"{row[0]:<20} {row[1]:<20} {row[2]:<15} {row[3]:<15} {row[4]:<15} {row[5]:<15}")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    get_tables_info()