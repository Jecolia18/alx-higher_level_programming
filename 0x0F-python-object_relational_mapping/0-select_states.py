#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":

    data_base = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)

    curs = data_base.cursor()
    curs.execute("SELECT * FROM states")
    row = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    database.close()
