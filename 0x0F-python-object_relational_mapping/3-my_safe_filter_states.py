#!/usr/bin/python3
"""MySQLdb module for python (MySQL Python) usage
returns a query where a specified name is searched
with SQL injection avoided
"""
import MySQLdb
import sys
import re

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
    regex_composite = re.compile(r"^[\w\"\']+[\w ]+[\"\']?")
    state_name = regex_composite.fullmatch(sys.argv[4])
    try:
        curs.execute("SELECT * FROM states WHERE states.name = '{}'\
 ORDER BY states.id ASC".format(state_name.group(0)))
    except:
        print("Missing state name")
        exit(1)

    query_res = curs.fetchall()
    if query_res:
        for row in query_res:
            print(row)
    curs.close()
    db_conn.close()
