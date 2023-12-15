# !/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":  # Ensure the script won't be executed when imported
    # Fetch command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to fetch states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display all states
    for state in cursor.fetchall():
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
