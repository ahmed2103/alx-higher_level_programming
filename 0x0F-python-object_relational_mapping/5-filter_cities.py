#!/usr/bin/python3

"""
script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    state_name = argv[4]
    cur.execute("""SELECT cities.name FROM cities 
                    INNER JOIN states ON cities.state_id = states.id
                    WHERE states.name = %s""", (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row[0])
    cur.close()
    conn.close()
