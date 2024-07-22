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

    def ex(conn, q):
        """execute"""
        cu = conn.cursor()
        cu.execute(q)
        r = cu.fetchall()
        cu.close()
        return r

    conne = conc("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    q = (
            "SELECT * FROM states WHERE name LIKE BINARY '{}'"
            "ORDER BY states.id").format(sys.argv[4])
    rows = ex(conne, q)
    for i in rows:
        print(i)
    conne.close()
