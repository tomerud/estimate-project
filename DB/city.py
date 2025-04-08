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
        ("Paris", "France", 2.3522, 48.8566),
        ("London", "United Kingdom", -0.1276, 51.5074),
        ("Tokyo", "Japan", 139.6917, 35.6895),
        ("Sydney", "Australia", 151.2093, -33.8688),
        ("Wellington", "New Zealand", 174.7762, -41.2865),
        ("Seoul", "South Korea", 126.9780, 37.5665),
        ("Rome", "Italy", 12.4964, 41.9028),
        ("Madrid", "Spain", -3.7038, 40.4168),
        ("Amsterdam", "Netherlands", 4.9041, 52.3676),
        ("Stockholm", "Sweden", 18.0686, 59.3293),
        ("Oslo", "Norway", 10.7522, 59.9139),
        ("Copenhagen", "Denmark", 12.5683, 55.6761),
        ("Helsinki", "Finland", 24.9354, 60.1695),
        ("Zurich", "Switzerland", 8.5417, 47.3769),
        ("Vienna", "Austria", 16.3738, 48.2082),
        ("Brussels", "Belgium", 4.3517, 50.8503),
        ("Dublin", "Ireland", -6.2603, 53.3498),
        ("Singapore", "Singapore", 103.8198, 1.3521),
        ("Beijing", "China", 116.4074, 39.9042),
        ("Mumbai", "India", 72.8777, 19.0760),
        ("Rio de Janeiro", "Brazil", -43.1729, -22.9068),
        ("Moscow", "Russia", 37.6173, 55.7558),
        ("Cape Town", "South Africa", 18.4241, -33.9249),
        ("Mexico City", "Mexico", -99.1332, 19.4326),
        ("Buenos Aires", "Argentina", -58.3816, -34.6037),
        ("Santiago", "Chile", -70.6483, -33.4489),
        ("Bogota", "Colombia", -74.0721, 4.7110),
        ("Istanbul", "Turkey", 28.9784, 41.0082),
        ("Riyadh", "Saudi Arabia", 46.6753, 24.7136),
        ("Dubai", "United Arab Emirates", 55.2708, 25.2048),
        ("Cairo", "Egypt", 31.2357, 30.0444),
        ("Jakarta", "Indonesia", 106.8456, -6.2088),
        ("Hanoi", "Vietnam", 105.8545, 21.0285),
        ("Bangkok", "Thailand", 100.5018, 13.7563),
        ("Kuala Lumpur", "Malaysia", 101.6869, 3.1390),
        ("Manila", "Philippines", 120.9842, 14.5995)
    ]

    # Insert each city into the database
    for city_name, country_name, longitude, latitude in cities:
        insert_city(city_name, country_name, longitude, latitude)