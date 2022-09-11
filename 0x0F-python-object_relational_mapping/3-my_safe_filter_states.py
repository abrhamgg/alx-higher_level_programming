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
    if sys.argv[4]:
        if ';' in sys.argv[4]:
            new = sys.argv[4].split(';')
            checked_sql = new[0].strip('\"')
            print(checked_sql)
        else:
            checked_sql = sys.argv[4]
        print(checked_sql)
    r.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY `id` ASC".format(checked_sql))
    [print(state) for state in r.fetchall() if state[1] in checked_sql]
