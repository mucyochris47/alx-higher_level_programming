import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    # Query to get cities based on the state name
    query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id
    """
    
    cursor.execute(query, (state_name,))

    # Fetch all results
    cities = cursor.fetchall()

    # Print the result
    if cities:
        for city in cities:
            print(f"{city[0]}: {city[1]}")
    else:
        print("No cities found for the state")

    # Close the connection
    cursor.close()
    db.close()

