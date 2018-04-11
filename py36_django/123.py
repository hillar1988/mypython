import  pymssql
def dbaccess():
    conn = pymssql.connect(host='154.24.2.9', user='sa', password='sa!@#456', database='ESNT')
    cur = conn.cursor()
    cur.execute('select top 10 * from [ESNT].[dbo].[UDT$BLFMMAST_hall]')
    ret = cur.fetchall()
    conn.close()
    cur.close()
    return ret


print(dbaccess())