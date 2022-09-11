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
    checked_sql = ''
    if sys.argv[4] and ';' in sys.argv[4]:
        checked_sql = sys.argv[4].split(';')
    else:
        checked_sql = sys.argv[4]
        r.execute("SELECT * FROM states WHERE name LIKE"
                  "'{}' ORDER BY `id` ASC".format(sys.argv[4]))
    [print(state) for state in r.fetchall() if state[1] == sys.argv[4]]
