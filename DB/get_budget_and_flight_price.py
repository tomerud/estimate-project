import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_budget_and_flight_price(origin, destination, month, travel_type):
    """
    Retrieves the daily budget for the destination city and the flight price
    from the origin to the destination for the specified month.
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

            # Get the destination city's budget based on travel type
            budget_query = f"""
            SELECT 
                CASE 
                    WHEN %s = 'backpacker' THEN backpacker_budget
                    WHEN %s = 'average' THEN avg_budget
                    WHEN %s = 'expensive' THEN expensive_budget
                END AS daily_budget
            FROM cities
            WHERE city_name = %s;
            """
            cursor.execute(budget_query, (travel_type, travel_type, travel_type, destination))
            budget_result = cursor.fetchone()

            if not budget_result or budget_result[0] is None:
                print(f"No budget information found for destination: {destination}")
                return None

            daily_budget = budget_result[0]

            # Get the destination_id for the destination city
            destination_id_query = "SELECT city_id FROM cities WHERE city_name = %s;"
            cursor.execute(destination_id_query, (destination,))
            destination_id_result = cursor.fetchone()

            if not destination_id_result:
                print(f"No destination_id found for city: {destination}")
                return None

            destination_id = destination_id_result[0]

            # Determine the flight prices table name based on the origin
            origin_parts = origin.lower().split()
            if len(origin_parts) == 1:
                flight_table = f"{origin_parts[0]}_flight_prices"
            else:
                flight_table = f"{origin_parts[0]}_{origin_parts[1]}_flight_prices"

            # Get the flight price for the specified month
            flight_price_query = f"""
            SELECT {month.lower()}_flight_price
            FROM {flight_table}
            WHERE destination_id = %s;
            """
            cursor.execute(flight_price_query, (destination_id,))
            flight_price_result = cursor.fetchone()

            if not flight_price_result or flight_price_result[0] is None:
                print(f"No flight price found for destination: {destination} in month: {month}")
                return None

            flight_price = flight_price_result[0]

            # Return the daily budget and flight price
            return {
                "daily_budget": daily_budget,
                "flight_price": flight_price
            }

    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Example usage
if __name__ == "__main__":
    result = get_budget_and_flight_price(
        origin="Tel Aviv",
        destination="berlin",
        month="January",
        travel_type="backpacker"
    )
    if result:
        print(f"Daily Budget: {result['daily_budget']}")
        print(f"Flight Price: {result['flight_price']}")