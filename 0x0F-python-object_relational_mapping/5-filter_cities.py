#!/usr/bin/python3
"""MySQLdb module for python (MySQL Python) usage
returns all cities by state
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
        curs.execute("SELECT cities.name FROM cities\
 JOIN states ON cities.state_id = states.id WHERE states.name = '{}'\
 ORDER BY cities.id ASC".format(sys.argv[4]))
    except:
        exit(1)

    query_res = curs.fetchall()
    list_states = []
    if query_res:
        for row in query_res:
            list_states.append(row[0])
    print(", ".join(list_states))
    curs.close()
    db_conn.close()
