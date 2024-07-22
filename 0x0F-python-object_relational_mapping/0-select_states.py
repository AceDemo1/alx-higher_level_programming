#!/usr/bin/python3
import MySQLdb
import sys

def conc(na, ur, pa, db):
    conn = MySQLdb.connect(
            host=na, user=ur,
            password=pa, database=db, port=3306)
    return conn

def ex(conn, q):
    cu = conn.cursor()
    cu.execute(q)
    r = cu.fetchall()
    cu.close()
    return r

conne = conc('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
q = 'SELECT * FROM state'
rows = ex(conne, q)
for i in rows:
    print(i)
conne.close()    
