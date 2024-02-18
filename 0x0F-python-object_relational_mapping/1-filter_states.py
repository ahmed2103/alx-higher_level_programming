#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database `hbtn_0e_0_usa`
"""
if __name__ == "__main__":
    import sys
    import MYSQLdb

    """establish connection to database"""
    db = MYSQLdb.connect(host = 'localhost'user=sys.argv[1], passwd=sys, db=sys.argv[2],
                         port = 3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE '%N' ORDER BY id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()