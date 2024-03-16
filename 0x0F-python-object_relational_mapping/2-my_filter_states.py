#!/usr/bin/python3
"""Lists all the tuples of a table states
  with a name starting with upper N
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=dbname)
    cur = db.cursor()
    format = "SELECT * FROM states WHERE states.name=%s\
                ORDER BY states.id"
    cur.execute(format, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
