#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":

    connector = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    myCursor = connector.cursor()
    myCursor.execute("SELECT * FROM states ORDER BY states.id")
    records = myCursor.fetchall()

    for record in records:
        print(record)

    connector.close()
