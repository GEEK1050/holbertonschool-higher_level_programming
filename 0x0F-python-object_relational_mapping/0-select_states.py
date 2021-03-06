#!/usr/bin/python3
"""
print states from database
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    dataBase = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3])

    cursor = dataBase.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for element in rows:
        print(element)

    cursor.close()
    dataBase.close()
