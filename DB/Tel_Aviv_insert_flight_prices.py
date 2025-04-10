import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import random

# Load environment variables from .env file
load_dotenv()

def generate_monthly_prices(january_price):
    """Generate flight prices for the rest of the months based on January's price."""
    return [random.randint(january_price - 30, january_price + 30) for _ in range(11)]

def insert_flight_prices():
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

            # Query to get cities and their continent
            query = """
            SELECT c.city_id, c.city_name, co.continent_id
            FROM cities c
            JOIN countries co ON c.country_id = co.country_id;
            """
            cursor.execute(query)
            cities = cursor.fetchall()

            for city_id, city_name, continent_id in cities:
                # Determine the price range based on the continent
                if continent_id == 3:  # Europe
                    january_price = random.randint(280, 400)
                elif continent_id == 1:  # Asia
                    january_price = random.randint(500, 800)
                elif continent_id == 2:  # Africa
                    january_price = random.randint(380, 600)
                elif continent_id in [4, 5]:  # North or South America
                    january_price = random.randint(800, 1000)
                elif continent_id == 7:  # Australia
                    january_price = random.randint(1000, 1400)
                else:
                    print(f"Unknown continent for city {city_name}. Skipping...")
                    continue

                # Generate prices for the rest of the months
                monthly_prices = [january_price] + generate_monthly_prices(january_price)

                # Insert the data into the tel_aviv_flight_prices table
                insert_query = """
                INSERT INTO tel_aviv_flight_prices (
                    destination_id, jan_flight_price, feb_flight_price, mar_flight_price,
                    apr_flight_price, may_flight_price, jun_flight_price, jul_flight_price,
                    aug_flight_price, sep_flight_price, oct_flight_price, nov_flight_price,
                    dec_flight_price
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                cursor.execute(insert_query, (city_id, *monthly_prices))

            # Commit the changes
            connection.commit()
            print("Flight prices inserted successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    insert_flight_prices()