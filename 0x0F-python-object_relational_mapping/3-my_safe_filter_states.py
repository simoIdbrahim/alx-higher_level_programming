#!/usr/bin/python3
""" displays all values in the states table """

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY \
        %s ORDER BY states.id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for state in rows:
        print(state)

    cursor.close()
    db.close()
