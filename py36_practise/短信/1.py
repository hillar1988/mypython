import pandas as pd
ls=pd.DataFrame(pd.read_excel('duanxin.xlsx',header=None))
'''ls.shape[0]:取行数；ls[0][i]：第一列的数据'''
for i in range(0,ls.shape[0]):
    print(ls[0][i],"+",ls[1][i])