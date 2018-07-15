# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 10:56:03 2018

"""

# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
# http://initd.org/psycopg/docs/usage.html
# http://www.postgresqltutorial.com/postgresql-python/create-tables/

import psycopg2

try:
    conn = psycopg2.connect("dbname='study' user='quant' host='localhost' password='quant'")
except:
    print("I am unable to connect to the database")
    
print(conn)

cur = conn.cursor()

cur.execute("""SELECT * from Persons""")

rows = cur.fetchall()

print ("\nShow me the databases:\n")
for row in rows:
    print ("   ", row)
