import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s"
    cursor.execute(query, (state_name,))

    # Fetch and print the result
    result = cursor.fetchone()
    if result:
        print(result)
    else:
        print("Not found")
    
    # Close the connection
    cursor.close()
    db.close()

