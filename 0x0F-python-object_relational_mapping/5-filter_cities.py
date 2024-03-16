#!/usr/bin/python3
"""Takes in name of a state and lists all cities
of that state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON\
                cities.state_id=states.id WHERE BINARY states.name=%s\
                ORDER BY cities.id", (state_name,))
    rows = cur.fetchall()
    names = []
    for row in rows:
        names.append(str(row).replace('(\'', '').replace('\',)', ''))

    for i in range(len(names) - 1):
        print(names[i], end=", ")

    if names:
        print(names[-1])
