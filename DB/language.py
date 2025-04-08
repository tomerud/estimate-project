import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def insert_language(language_name):
    """
    Inserts a language into the `languages` table.
    Checks if the language already exists before inserting.
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

            # Check if the language already exists
            check_language_query = """
            SELECT COUNT(*) FROM languages WHERE language_name = %s;
            """
            cursor.execute(check_language_query, (language_name,))
            result = cursor.fetchone()

            if result[0] > 0:
                print(f"Language '{language_name}' already exists in the database. Skipping insertion.")
            else:
                # SQL to insert a new language
                insert_language_query = """
                INSERT INTO languages (language_name)
                VALUES (%s);
                """

                # Execute the query with the provided value
                cursor.execute(insert_language_query, (language_name,))

                # Commit the changes
                connection.commit()

                print(f"Language '{language_name}' inserted successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    # List of languages to insert
    languages = [
        "English",
        "Spanish",
        "Slavic",
        "Asian",
        "Arabic",
        "Other"
                ]

    # Insert each language into the database
    for language_name in languages:
        insert_language(language_name)