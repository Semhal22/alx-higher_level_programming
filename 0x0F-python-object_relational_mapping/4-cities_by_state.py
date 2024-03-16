#!/usr/bin/python3
"""Lists all cities by joining the two tables"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM\
                cities JOIN states WHERE state_id = states.id\
                ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
