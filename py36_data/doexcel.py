import xlrd
data = xlrd.open_workbook('33.xls')
table = data.sheet_by_name(u'Sheet1')
print(table.row_values(5))