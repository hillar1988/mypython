'''
SQLSERVER数据库
'''
# import pymssql
# conn=pymssql.connect(host='154.24.2.9',user='sa',password='sa!@#456',database='ESNT')
# cur=conn.cursor()
# cur.execute('SELECT TOP 10 * FROM [ESNT].[dbo].[UDT$BLFMCURS]')
# #如果update/delete/insert记得要conn.commit()
# #否则数据库事务无法提交
# print (cur.fetchall()[0])
# cur.close()
# conn.close()
'''
DB2数据库
'''
# import ibm_db
# connstr="DATABASE=dmfhdb;HOSTNAME=154.30.16.11;PORT=50004;PROTOCOL=TCPIP;UID=fhdba;PWD=fhdbaxgb;"
# conn = ibm_db.connect(connstr,"","")
# if conn:
#     sql = "Select  * from DMFH.CCRD_CARD fetch first 10 rows only"
#     stmt = ibm_db.exec_immediate(conn, sql)
#     result = ibm_db.fetch_both(stmt)
#     while( result ):
#         print ("员工编号 :", result[0] +'\n'+ "姓名:",result[1] +'\n'+ "生日:",result[2])
#         print ('-----------------')
#         result = ibm_db.fetch_both(stmt)
'''
mysql数据库
'''
# import pymysql
# # 打开数据库连接
# db = pymysql.connect("154.24.8.87", "bigdata", "Hidata.2017", "os")
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT * FROM user_info;")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print(data)
# # 关闭数据库连接
# db.close()
'''
sqlite3数据库
'''
import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print ("Table created successfully")
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)  VALUES (1, 'Paul', 32, 'California', 20000.00 )")
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)  VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)  VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)  VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
conn.commit()
ret=c.execute("select * from COMPANY").fetchone()
print(ret)
conn.close()