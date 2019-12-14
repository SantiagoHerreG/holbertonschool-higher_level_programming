#!/usr/bin/python3
"""MySQLdb module for python (MySQL Python) usage
"""
import MySQLdb
import sys

if __name__ == "__main__":
"""The code is not executed when imported
"""

    db_conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    curs = db_conn.cursor()
    curs.execute("SELECT * FROM states ORDER BY states.id ASC")

    query_res = curs.fetchall()
    for row in query_res:
        print(row)
    curs.close()
    db_conn.close()
