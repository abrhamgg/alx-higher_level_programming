#!/usr/bin/python3
"""
List all states with the name given in the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    r = db.cursor()
    r.execute("SELECT * FROM states WHERE name = '{}' ORDER BY `id`".format(sys.argv[4]))
    [print(state) for state in r.fetchall()]
