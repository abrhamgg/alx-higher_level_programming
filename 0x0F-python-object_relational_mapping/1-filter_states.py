#!/usr/bin/python3
"""
List all states with the name starting with 'N'
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    r = db.cursor()
    r.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY `id`")
    [print(state) for state in r.fetchall()]
