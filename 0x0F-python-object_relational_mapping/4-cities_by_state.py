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
            'SELECT cities.id states cities'
            'FROM cities JOIN state ON state_id=cities.id'
            'ORDER BY cities.id')
    rows = ex(conne, q)
    for i in rows:
        print(i)
    conne.close()
