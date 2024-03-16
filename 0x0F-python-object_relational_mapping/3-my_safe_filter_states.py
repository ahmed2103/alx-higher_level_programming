#!/usr/bin/python3

"""
safe script to do previous sql query
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user = argv[1],
                           passwd = argv[2],
                           db = argv[3])
    cur = conn.cursor()
    safe = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (safe, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
