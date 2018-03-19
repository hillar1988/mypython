# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# for i in d:
#  print(d[i])
'''
计算从1到1000的累计值。
'''
# sum=0
# for i in range(1001):
#  sum=sum+i
# print(sum)
'''
计算从1到1000的偶数之和。
'''
# sum=0
# for i in range(11):
#  if i%2==0:
#   sum=sum+i
# print(sum)
'''
字符串的一些功能
'''
# t = 'He is a string. Who are you?'
# print(t.capitalize()) # Cap first letter
# print(t.split()) # split by words
# print(t.find('i')) # return index of 'i'
# print(t.find('in')) # index of 'i' in 'in'
# print(t.find('Python')) # find sth not in
# print(t[0:4]) # returu from index 0 to 3
# print(t.replace(' ','|')) # replace by '|'
# w = 'http://www.google.com'
# print(w.strip('http://')) #delete sth
'''
求两个变量最大值的函数
'''
# def  MaxOfTwo (x1, x2):
#      if  x1 >= x2:
#           return x1
#      else:
#           return x2
# a = 1
# b = 2
# c = MaxOfTwo(a, b)
# print(c)
'''
创建一个文件 (Creating new file)
这个mode参数可以是（The mode can be）
'r' 只读模式（when the file will only be read）
'w' 只写模式（与一个现存文件文件同名，则被清除）
'a' 添加模式，即任意写入文件的数据都被自动添加到末尾
'r+' 打开文件，可以读、写
'''
# file=open('first.txt','w')
# file.write('I am created for the course. \n')
# file.write('How about you? ')
# file.write('How is your exam?')
# file.close()
'''
读取一个文件 (Reading a file)
'''
# file = open('first.txt', 'r')
# #show whole efile
# print(file.read())
# #show first ten characterrs
# print(file.read(10))
# #view by line
# print(file.readline())
# #view all by line
# print(file.readlines())
# file.close()
'''
循环读取一个文件 (Looping over a file object)
'''
# file = open('first.txt', 'r')
# for  line  in  file:
#      print (line)
# file.close()
'''
增加一个文件 (Adding in a file)
'''
# file = open('first.txt', 'a')
# file.write('\nI am back again. \n')
# file.write('Do  you miss me?\n')
# file.close()
'''
with语句 (The with statement)
很容易忘记关闭{close()}文件。 由于这个和其他原因，最好使用with语句:
'''
# with open("first.txt") as f:
#  print(f.read())
'''
这样可以确保文件正确关闭，即使读取时发生错误。
文件路径 (File paths)
也可以使用绝对路径指定文件名。
示例（Mac / Linux）：
open ('/etc/gimp/2.O/gtkrc')
示例（Windows）：
open('C:\Documents\file.txt')
请注意，反斜杠需要转义（写入两次'\'）
'''
'''
阶乘的应用
'''
# def fact(n):
#  if n==1:
#   return 1
#  return n*fact(n-1)
# print(fact(5)) #120的阶乘
'''
斐波那契数列
'''
# def fei(n):
#  a1=1
#  if n==1 or n==2:
#   return a1
#  else:
#   return fei(n-2)+fei(n-1)
# total=[]
# for i in range(1,11):
#  total.append(fei(i))
# print(total)
'''
尝试导入模块时间，并使用它来获取计算机运行特定代码所需的时间。
'''
# import timeit
# def funl(x,y):
#  return x**2+y**3 #我记得x*2是x乘以2，x**2是x的二次方
# t_start=timeit.default_timer()
# z=funl(109.2,367.1) #计算这个乘方的时间
# t_end=timeit.default_timer()
# cost=t_end-t_start
# print('Time cost of funl is %f'%cost)
'''
创建numpy数组
'''
#import numpy as np
# In [1] : np.array([2, 3, 6, 7])
# Out[l] : array([2, 3, 6, 7])
# In [2] : np.array([2, 3, 6, 7.])
# Out [2] :  array([ 2.,  3.,  6., 7.])  <- Hamogenaous
# In  [3] :  np.array( [2,  3,  6,  7+ij])
# Out [3] :  array([ 2.+O.j,  3.+O.j,  6.+O.j,  7.+1.j])
'''
创建均匀间隔的数组
'''
# arange：
# in[1]：np.arange（5）
# Out [l]：array（[0，1，2，3，4]）
# range(start, stop, step)的所有三个参数即起始值，结束值，步长都是可以用的 另外还有一个数据的dtype参数
# in[2]：np.arange（10，100，20，dtype = float）
# Out [2]：array（[10.，30.，50.，70.，90.]）
# linspace（start，stop，num）返回数字间隔均匀的样本，按区间[start，stop]计算：
# in[3]：np.linspace（0.，2.5，5）# 这在生成plots图表中非常有用。注释：即从0开始，到2.5结束，然后分成5等份
# Out [3]：array([0.，0.625，1.25，1.875，2.5])
'''
多维数组矩阵 (Matrix by multidimensional array)
'''
# In [1] : a = np.array([[l, 2, 3]  [4, 5, 6]])
#                           ^ 第一行 (Row 1)
# In  [2] : a
# Out [2] : array([[l, 2,  3] ,   [4,  5,  6]])
# In  [3] : a.shape  #<- 行、列数等 (Number of rows, columns etc.)
# Out [3] : (2,3)
# In  [4] : a.ndim   #<- 维度数  (Number of dimensions)
# Out [4] : 2
# In  [5] : a.size   #<- 元素数量 (Total number of elements)
# Out [5] : 6
# import numpy as np
# a = np.array([1,2,3,4,5])
# b = a.copy ()
# c1 =  np.dot(np.transpose(a), b)
# print(c1)
# c2  = np.dot(a, np.transpose(b))
# print(c2)
# ax  =  np.reshape(a, (5,1))
# bx  =  np.reshape(b, (1,5))
# c = np.dot(ax, bx)
# print(c)
# print(np.random.rand(2, 4)) # 0和1之间均匀分布的随机数
'''
线性方程的解  (Solution of linear equations:)
'''
# import numpy as np
# from scipy import linalg
#
# A = np.random.randn(5, 5)
# b = np.random.randn(5)
# x = linalg.solve(A, b)     # A x = b#print(x)
# eigen = linalg.eig(A)     # eigens#print(eigen)
# det = linalg.det(A)     # determinant
# print(b)
# print(det)
'''
数值整合 (Numerical integration)
'''
# import numpy as np
# from scipy import integrate
# def fun(x):
#     return np.log(x)
# value, error = integrate.quad(fun,0,1)
# print(value)
# print(error)
'''
最简单的制图 (The simplest plot)
'''
# import numpy as np
# from scipy.optimize import curve_fit
# import matplotlib.pyplot as plt
#
# def func(x, a, b, c):
#
#     return a * np.exp(-b * x) + c
#
# x = np.linspace(0, 4, 50)
# y = func(x, 2.5, 1.3, 0.5)
# ydata = y+0.2*np.random.normal(size=len(x))
# popt, pcov = curve_fit(func, x, ydata)
# plt.plot(x,ydata, 'b*')
# plt.plot(x, func(x, popt[0], \
#                     popt[1], popt[2]), 'r-')
# plt.title('$f(x)=ae^{-bx}+c$ curve fitting')
# plt.show()
'''
多个制图图例标签和标题 (Multiple plotting, legends, labels and title)
'''
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(0, 10, 201)
# plt.figure(figsize = (4, 4))
# for n in range(2, 5):
#     y = x ** (1 / n)
#     plt.plot(x, y, label='x^(1/' \
#             + str(n) + ')')
# plt.legend(loc = 'best')
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
# plt.xlim(-2, 10)
# plt.title('Multi-plot e.g. ', fontsize = 18)
# plt.show()
'''
绘制子图
'''
# import numpy as np
# import matplotlib.pyplot as plt
#
# def pffcall(S, K):
#     return np.maximum(S - K, 0.0)
# def pffput(S, K):
#     return np.maximum(K - S, 0.0)
#
# S = np.linspace(50, 151, 100)
# fig = plt.figure(figsize=(12, 6))
#
# sub1 = fig.add_subplot(121)     # col, row, num
# sub1.set_title('Call', fontsize = 18)
# plt.plot(S, pffcall(S, 100), 'r-', lw = 4)
# plt.plot(S, np.zeros_like(S), 'black',lw = 1)
# sub1.grid(True)
# sub1.set_xlim([60, 120])
# sub1.set_ylim([-10, 40])
#
# sub2 = fig.add_subplot(122)
# sub2.set_title('Put', fontsize = 18)
# plt.plot(S, pffput(S, 100), 'r-', lw = 4)
# plt.plot(S, np.zeros_like(S), 'black',lw = 1)
# sub2.grid(True)
# sub2.set_xlim([60, 120])
# sub2.set_ylim([-10, 40])
# plt.show()
'''
绘制3D图形
'''
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import cm
# from mpl_toolkits.mplot3d import Axes3D
#
# x, y = np.mgrid[-5:5:100j, -5:5:100j]
# z = x**2 + y**2
# fig = plt.figure(figsize=(8, 6))
# ax = plt.axes(projection='3d')
# surf = ax.plot_surface(x, y, z, rstride=1,\
#                        cmap=cm.coolwarm, cstride=1, \
#                        linewidth=0)
# fig.colorbar(surf, shrink=0.5, aspect=5)
# plt.title('3D plot of $z = x^2 + y^2$')
# plt.show()
'''
符号的使用
'''
# import sympy as sy
#
# #声明x，y为变量
# x = sy.Symbol('x')
# y = sy.Symbol('y')
# a, b = sy.symbols('a b')
#
# #创建一个新符号（不是函数
# f = x**2 + 2 - 2*x + x**2 -1
# print(f)
# #自动简化
# g = x**2 + 2 - 2*x + x**2 -1
# print(g)
sum((i for i in range(10)))