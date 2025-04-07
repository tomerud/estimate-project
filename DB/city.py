import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def insert_city(city_name, country_name, longitude, latitude):
    """
    Inserts a city into the `cities` table.
    Finds the `country_id` based on the given `country_name`.
    Checks if the city already exists before inserting.
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

            # Find the country_id for the given country_name
            find_country_query = """
            SELECT country_id FROM countries WHERE country_name = %s;
            """
            cursor.execute(find_country_query, (country_name,))
            result = cursor.fetchone()

            if result:
                country_id = result[0]

                # Check if the city already exists
                check_city_query = """
                SELECT COUNT(*) FROM cities WHERE city_name = %s AND country_id = %s;
                """
                cursor.execute(check_city_query, (city_name, country_id))
                city_result = cursor.fetchone()

                if city_result[0] > 0:
                    print(f"City '{city_name}' already exists in the database. Skipping insertion.")
                else:
                    # SQL to insert a new city
                    insert_city_query = """
                    INSERT INTO cities (city_name, country_id, longitude, latitude)
                    VALUES (%s, %s, %s, %s);
                    """

                    # Execute the query with the provided values
                    cursor.execute(insert_city_query, (city_name, country_id, longitude, latitude))

                    # Commit the changes
                    connection.commit()

                    print(f"City '{city_name}' inserted successfully.")
            else:
                print(f"Country '{country_name}' not found in the database. Cannot insert city '{city_name}'.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    # Example usage: Insert cities
    cities = [
        ("Tel Aviv", "Israel", 34.7818, 32.0853),
        ("New York", "United States", -74.0060, 40.7128),
        ("Toronto", "Canada", -79.3832, 43.6532),
        ("Berlin", "Germany", 13.4050, 52.5200),
        ("Paris", "France", 2.3522, 48.8566)
    ]

    # Insert each city into the database
    for city_name, country_name, longitude, latitude in cities:
        insert_city(city_name, country_name, longitude, latitude)