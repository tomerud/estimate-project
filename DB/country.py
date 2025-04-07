import mysql.connector
from mysql.connector import Error

def insert_country(country_name, hdi):
    """
    Inserts a country and its HDI into the `countries` table.
    Checks if the country already exists before inserting.
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
                INSERT INTO countries (country_name, hdi)
                VALUES (%s, %s);
                """

                # Execute the query with the provided values
                cursor.execute(insert_country_query, (country_name, hdi))

                # Commit the changes
                connection.commit()

                print(f"Country '{country_name}' with HDI {hdi} inserted successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    # List of countries with their HDI values
    countries = [
        ("Israel", 0.919),
        ("United States", 0.926),
        ("Canada", 0.929),
        ("Germany", 0.936),
        ("France", 0.891),
        ("United Kingdom", 0.929),
        ("Japan", 0.915),
        ("Australia", 0.951),
        ("New Zealand", 0.937),
        ("South Korea", 0.925),
        ("Italy", 0.892),
        ("Spain", 0.904),
        ("Netherlands", 0.944),
        ("Sweden", 0.945),
        ("Norway", 0.961),
        ("Denmark", 0.948),
        ("Finland", 0.940),
        ("Switzerland", 0.955),
        ("Austria", 0.922),
        ("Belgium", 0.931),
        ("Ireland", 0.955),
        ("Singapore", 0.939),
        ("China", 0.768),
        ("India", 0.633),
        ("Brazil", 0.754),
        ("Russia", 0.822),
        ("South Africa", 0.713),
        ("Mexico", 0.758),
        ("Argentina", 0.842),
        ("Chile", 0.855),
        ("Colombia", 0.752),
        ("Turkey", 0.838),
        ("Saudi Arabia", 0.875),
        ("United Arab Emirates", 0.911),
        ("Egypt", 0.731),
        ("Indonesia", 0.705),
        ("Vietnam", 0.703),
        ("Thailand", 0.800),
        ("Malaysia", 0.803),
        ("Philippines", 0.699)
    ]

    # Insert each country into the database
    for country_name, hdi in countries:
        insert_country(country_name, hdi)