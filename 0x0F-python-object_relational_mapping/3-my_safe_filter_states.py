#!/usr/bin/python3
"""
modified script to prevent MYSQL injection when attempting to use malicious query
"""
from sys import argv
import MYSQLdb
if __name__ == "__main__":
    db = MYSQLdb.connect(user=argv[1], passwd=argv[2], host="localhost"
                         , db = argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name like %s BY id in ASC",
                 argv[4])
    for row in curs.fetchall:
        print(row)
    curs.close()
    db.close()