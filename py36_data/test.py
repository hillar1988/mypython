import pymssql
import pandas  as pd
import numpy as np
#通过read_sql直接从数据库获取数据
conn = pymssql.connect(host='127.0.0.1',user='sa',password='sa',database='BOOK',charset='utf8')
sql = 'select * from student'
df=pd.read_sql(sql,conn)
#print(df.head(1))
#print(df.dtypes)
#dates=pd.date_range('20160728',periods=6)#创建固定频度的时间序列
#df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD')) #创建6*4的随机数，索引，列名称。
#df2=pd.DataFrame({'A':pd.Timestamp('20160728'),'B':pd.Series(1)})#字典创建Dataframe，假如字典的数据长度不同，以最长的数据为准。
df2=pd.DataFrame({'A':np.arange(1,10,2),'B':range(1,10,2)})#字典创建Dataframe
# print(df2.describe())
#print(df2.T)#转置
#print(df2[0:2])#切片得到的是行数据
#print(df2.loc[0:2,['A','B']])#选择多列数据
#print(df2.loc['0':'2',['A','B']]) #选择局部区域
#print(df2.iloc[3]) #提取第四行数据,取第2行第2列的这个数,df2.iloc[1,1]
#print(df2.iat[0,0])#专门取某个数，效率比较高
#print(df2[(df2.A>2)&(df2.B<5)])#删选：a列大于2，B列小于5的数据
#alist=[1,3]
#print(df2[df2['A'].isin(alist)]) #删选：提取A列的值在alist中的行
#counts=df2[u'A'].value_counts()#计算A列各个值的数量
# plt=counts.plot(kind='bar').get_figure()
# plt.savefig('plot.png')  #画图
#df.groupby(['A','B']) #按两列分组
# print(df2.groupby('A').sum())
# df2['c']=pd.Series(np.random.randn(10))
# df2.insert(1,'e',df2['A'])#在a列后面插入e列
# print(df2)
'''
字符串的操作
'''
# s=pd.Series(list('ABCDEF'))
# s.str.lower()
# s.str.upper()#大小写
# s.str.len()
# s.str.split('_').str.get(1) #获取切割后的某个元素
# print(s.str.split('_').str.get(1))
# s=pd.Series(['a11','a21','b11','b21'])
# s.str.extract('([ab])(\d)?')#使用extract方法提取数字:第一个参数是正则表达式，括号表示要提取的部分
# print(s.str.extract('([abc])(\d\d)?'))
# pattern=r'[a-z][0-9]'
# print(s.str.contains(pattern,na=False))#匹配字符串，na参数用来说明出现NaN数据时匹配成True还是False
df=pd.DataFrame(np.random.randn(5,3),index=list(range(1,6,1)),columns=[2,3,4])
# df.ix[1,:-1]=np.nan #在简单的运算中，遇到缺失值，运算结果也是缺失值，在描述性统计中，Nan都是作为0进行运算
# df.fillna(0)#用0来填充
#a=df.fillna(method='pad')#用前一个数据代替NaN
# a=df.sort_values(['one'],ascending=True)  #按照列col1降序排列数据
#df.rename(columns=lambda x: x + 1)
# df2=pd.DataFrame({'d':['1.01','2.01'],'e':['2.01','2.01'],'a':['3.01','2.01']})
# df3=pd.DataFrame({'d':['1.01'],'f':['2.01'],'g':['3.01']})
#a = pd.merge(df2, df3, how='outer', on=['d'])#用merge进行外连接
#a=pd.concat([df, df2],axis=1,ignore_index=True,join='inner')#将df2中的列添加到df1的尾部,axis=1为列追加
print(a)