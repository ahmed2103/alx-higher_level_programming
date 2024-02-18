#!/usr/bin/python3
"""a script that lists all states from the database `hbtn_0e_0_usa`"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(user =sys.argv[1], passwd =sys.argv[2],db =sys.argv[3])
    curs = db.cursor()
    curs.execute('SELECT * FROM states ORDER BY id DESC')
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
