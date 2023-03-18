#!/usr/bin/python3
"""
    lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                                user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3],
                                charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                 FROM states\
                 INNER JOIN cities ON states.id = cities.state_id\
                 WHERE states.name LIKE %s\
                 ORDER BY cities.id ASC", (sys.argv[4], ))

    print(", ".join(row[0] for row in cur.fetchall()))

    cur.close()
    conn.close()
