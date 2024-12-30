#!/usr/bin/python3
"""
This script takes arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. The script
is safe from SQL injection.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db_connect.cursor()
    
    # Use parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db_connect.close()

