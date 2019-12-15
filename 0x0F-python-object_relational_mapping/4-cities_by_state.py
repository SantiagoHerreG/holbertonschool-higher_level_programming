#!/usr/bin/python3
"""MySQLdb module for python (MySQL Python) usage
returns all rows in a table
"""
import MySQLdb
import sys
if __name__ == "__main__":
    """The code is not executed when imported
    """
    try:
        db_conn = MySQLdb.connect(host="localhost", port=3306,
                                  user=sys.argv[1],
                                  passwd=sys.argv[2],
                                  db=sys.argv[3],
                                  charset="utf8")
    except:
        exit(1)
    curs = db_conn.cursor()
    try:
        curs.execute("SELECT cities.id, cities.name, states.name FROM cities\
 JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    except:
        exit(1)

    query_res = curs.fetchall()
    if query_res:
        for row in query_res:
            print(row)
    curs.close()
    db_conn.close()
