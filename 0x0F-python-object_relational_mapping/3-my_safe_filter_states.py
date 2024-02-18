#!/usr/bin/python3
"""
modified script to prevent MYSQL injection when attempting to use malicious query
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         host="localhost", db=argv[3])
    curs = db.cursor()
    
    curs.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                 (argv[4],))
    
    for row in curs.fetchall():
        print(row)
    
    curs.close()
    db.close()
