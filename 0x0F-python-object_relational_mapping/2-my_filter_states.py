#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
 in the states table of hbtn_0e_0_usa
where name matches the argument.
"""
if __name__ == "__main__":
    from sys import argv
    import MYSQLdb
    db = MYSQLdb.connect(host="localhost", user = argv[1],
                         passwd=argv[2], db=argv[3], port = 3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name = {} BY id in ASC"
                 .format(argv[4]))
    for row in curs.fetchall:
        print(row)
    curs.close()
    db.close()
