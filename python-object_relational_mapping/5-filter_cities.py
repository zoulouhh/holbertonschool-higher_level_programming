#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py username password dbname state_name")
        sys.exit(1)

    # Extract arguments
    username, password, dbname, state_name = sys.argv[1:]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    # Print cities as comma-separated values
    print(", ".join(row[0] for row in rows))

    # Clean up
    cursor.close()
    db.close()