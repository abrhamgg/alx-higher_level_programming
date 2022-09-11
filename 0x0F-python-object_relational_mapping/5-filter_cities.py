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
    r.execute('SELECT cities.id, cities.name, states.name FROM cities '
              'JOIN states ON cities.state_id = states.id '
              'WHERE states.name = "{}" '
              'ORDER BY cities.id ASC;'.format(sys.argv[4]))
    [print(city) for city in r.fetchall()]
