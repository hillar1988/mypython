# from impala.dbapi import connect
# conn = connect(host="154.24.8.83", port=10000, database="hive",user="hive", password="hive",auth_mechanism="PLAIN")
# cur = conn.cursor()
# print(cur = conn.cursor())
# cur.execute("Select  * from card.cdtyshzl limit 10")
# cur.fetchone()
# conn.close()
# from impala.dbapi import connect
# conn = connect(host='154.24.8.83', port=10000,database='hive',user='hive', password='hive',auth_mechanism='PLAIN')
# cursor = conn.cursor()
# # cursor.execute('SELECT * FROM card.cdtyshzl LIMIT 10')
# print (cursor.description) # prints the result set's schema
# # results = cursor.fetchall()
from pyhive import hive  # or import hive
cursor = hive.Connection(host='154.24.8.83', port=10000,database='hive',username='hive:hive')
cursor.execute('SELECT * FROM card.cdtyshzl LIMIT 10')
print(cursor.fetchone())

