#!/usr/bin/python3
"""lists all states"""
import MySQLdb
import sys


if __name__ == "__main__":
    def conc(na, ur, pa, db):
        """connection"""
        conn = MySQLdb.connect(
            host=na, user=ur,
            passwd=pa, database=db, port=3306)
        return conn

    def ex(conn, q, pa):
        """execute"""
        cu = conn.cursor()
        cu.execute(q, pa)
        r = cu.fetchall()
        cu.close()
        return r

    conne = conc("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    q = (
            "SELECT cities.name FROM cities JOIN states "
            "ON cities.state_id=states.id WHERE states.name=%s"
            "ORDER BY cities.id")
    rows = ex(conne, q, (sys.argv[4],))
    for i in range(len(rows)):
        print(rows[i][0], end=', ' if i < len(rows) - 1 else '')
    conne.close()
