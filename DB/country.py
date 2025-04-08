import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def insert_country(country_name, hdi, language_id):
    """
    Inserts a country, its HDI, and language_id into the `countries` table.
    Checks if the country already exists before inserting.
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

            # Check if the country already exists
            check_country_query = """
            SELECT COUNT(*) FROM countries WHERE country_name = %s;
            """
            cursor.execute(check_country_query, (country_name,))
            result = cursor.fetchone()

            if result[0] > 0:
                print(f"Country '{country_name}' already exists in the database. Skipping insertion.")
            else:
                # SQL to insert a new country
                insert_country_query = """
                INSERT INTO countries (country_name, hdi, language_id)
                VALUES (%s, %s, %s);
                """

                # Execute the query with the provided values
                cursor.execute(insert_country_query, (country_name, hdi, language_id))

                # Commit the changes
                connection.commit()

                print(f"Country '{country_name}' with HDI {hdi} and language_id {language_id} inserted successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    # List of countries with their HDI values and language_id
    countries = [
        ("Israel", 0.919, 6),  # Other (Hebrew)
        ("United States", 0.926, 1),  # English
        ("Canada", 0.929, 1),  # English (English and French, but English is chosen)
        ("Germany", 0.942, 6),  # Other (German)
        ("France", 0.903, 6),  # Other (French)
        ("United Kingdom", 0.932, 1),  # English
        ("Australia", 0.951, 1),  # English
        ("New Zealand", 0.937, 1),  # English
        ("Japan", 0.915, 4),  # Asian
        ("South Korea", 0.916, 4),  # Asian
        ("China", 0.768, 4),  # Asian
        ("India", 0.633, 4),  # Asian
        ("Brazil", 0.754, 6),  # Other (Portuguese)
        ("Russia", 0.822, 3),  # Slavic
        ("Mexico", 0.758, 2),  # Spanish
        ("Argentina", 0.842, 2),  # Spanish
        ("Chile", 0.855, 2),  # Spanish
        ("Colombia", 0.752, 2),  # Spanish
        ("Turkey", 0.838, 6),  # Other (Turkish)
        ("Saudi Arabia", 0.854, 5),  # Arabic
        ("Egypt", 0.731, 5),  # Arabic
        ("South Africa", 0.713, 6),  # Other (Multiple languages)
        ("Singapore", 0.935, 4),  # Asian
        ("Malaysia", 0.803, 4),  # Asian
        ("Thailand", 0.800, 4),  # Asian
        ("Vietnam", 0.703, 4),  # Asian
        ("Philippines", 0.699, 4),  # Asian
        ("Indonesia", 0.705, 4),  # Asian
        ("Pakistan", 0.544, 4),  # Asian
        ("Bangladesh", 0.661, 4),  # Asian
        ("Italy", 0.895, 6),  # Other (Italian)
        ("Spain", 0.904, 2),  # Spanish
        ("Netherlands", 0.944, 6),  # Other (Dutch)
        ("Sweden", 0.947, 6),  # Other (Swedish)
        ("Norway", 0.961, 6),  # Other (Norwegian)
        ("Denmark", 0.948, 6),  # Other (Danish)
        ("Finland", 0.940, 6),  # Other (Finnish)
        ("Switzerland", 0.955, 6),  # Other (Multiple languages)
        ("Austria", 0.914, 6),  # Other (German)
        ("Belgium", 0.937, 6),  # Other (Dutch, French, German)
        ("Ireland", 0.955, 1),  # English
        ("Portugal", 0.866, 6),  # Other (Portuguese)
        ("Greece", 0.888, 6),  # Other (Greek)
        ("Poland", 0.876, 3),  # Slavic
        ("Czech Republic", 0.889, 3),  # Slavic
        ("Hungary", 0.854, 3),  # Slavic
        ("Slovakia", 0.860, 3),  # Slavic
        ("Ukraine", 0.773, 3),  # Slavic
        ("Romania", 0.821, 6),  # Other (Romanian)
        ("Bulgaria", 0.816, 3),  # Slavic
        ("Croatia", 0.858, 3),  # Slavic
        ("Serbia", 0.806, 3),  # Slavic
        ("Slovenia", 0.917, 3),  # Slavic
        ("Estonia", 0.892, 6),  # Other (Estonian)
        ("Latvia", 0.866, 6),  # Other (Latvian)
        ("Lithuania", 0.882, 6),  # Other (Lithuanian)
    ]

    # Insert each country into the database
    for country_name, hdi, language_id in countries:
        insert_country(country_name, hdi, language_id)