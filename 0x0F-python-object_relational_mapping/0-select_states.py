#!/usr/bin/python3
"""
module that connect to MySQL server and execute some queries
"""
import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
r = db.cursor()
r.execute('SELECT * FROM `states`')
[print(i) for i in r.fetchall()]
