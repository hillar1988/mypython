# print(1.23e9)
# print("I'am \"OK\"")
# def my_abs(x):
#     if x>0:
#         return x
#     if x<=0:
#         return -x
# print(my_abs(-10))
# print('Hello, %s' % 'world')
# classmates = ['Michael', 'Bob', 'Tracy']
# print(classmates[0][-2:])
# classmates = ['Michael', 'Bob', 'Tracy']
# for classmate in classmates:
#     print(classmate)
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(1,3,5,7))
# d = {'a': 1, 'b': 2, 'c': 3}
# for v,d in d.items():
#     print(v,d)
# print(list(range(1,11)))
# [list(range(1,11))]
# print([x*x for x in range(1,11)])
# print([x*x for x in range(1,11) if x%2==0])
# print([x*n for x in range(1,11) for n in range(11,12)])
# def fn(x):
#     return x*x
# r=map(fn, [1,2,3])
# print(list(r))
#########Decorator
# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():' %func.__name__)
#         return func(*args,**kw)
#     return wrapper
# @log
# def now():
#     print("hello world----2019-07-23")
# now()
# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args,**kw):
#             print('%s %s():'%(text,func.__name__))
#             return func(*args,**kw)
#         return wrapper
#     return decorator
#
# @log('exec')
# def now():
#     print('2019-07-23')
# print(now.__name__)
# 'a test module'
#
# __author__='jsh'
#
# import  sys
# def my():
#     args=sys.argv
#     if len(args)==1:
#         print('hello world!')
#     elif len(args)==2:
#         print('hello %s!' %args[1])
#     else:
#         print('too many arguments!')
# print('it'+'\''+'s a test!')
# if __name__=='__main__':
#     my()
# class student():
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
# my=student('jsh','100')
# my1=student('jsh1','1001')
# print(my.name,my.score)
# print(my1.name,my1.score)
#
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
#     __slots__ = ('name', 'age')
# def run_twice(animal):
#     animal.run()
#     animal.run()
# class cat(Animal):
#     def run(self):
#         print('cat is running...')
# class dog(Animal):
#     def run(self):
#         print('dog is running...')
# # cat1=cat()
# # cat1.run_twice(cat1())
# # dog1=dog()
# # dog1.run_twice()
# run_twice(cat())
# run_twice(dog())
# class Student(object):
#
#     def get_score(self):
#         return self._score
#     def set_score(self,score):
#         if not isinstance(score,int):
#             raise ValueError('score must be integer')
#         if score<0 or score>100:
#             raise ValueError('score must be 0~100')
#         self._score=score
# s=Student()
# s.set_score(100)
# print(s.get_score())
# class student():
#     #把一个getter方法变成属性，只需要加上 @ property就可以了
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,score):
#         if not isinstance(score,int):
#             raise ValueError('value must be intgeter')
#         if score<0 or score>100:
#             raise ValueError('value must be 0~100')
#         self._score=score
# s=student()
# s.score=100
# print(s.score)
# class student(object):
#     #初始化数据
#     def __init__(self,score):
#         self._score=score
#     #设置可读可写属性
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,score):
#         self._score=score
#     #设置只读属性
#     @property
#     def age(self):
#         return 2015-self._score
# s=student(100)
# s.score=200
# print(s.age)
# class Animal(object):
#     pass
# class Mammal(Animal):
#     pass
# class Bird(Animal):
#     pass
# #################################
# class RunnableMixIn(object):
#     def run(self):
#         print('running...')
# class FlyableMixIn(object):
#     def fly(self):
#         print('flying...')
#
# class Dog(Mammal,RunnableMixIn):
#     pass
# class Bat(Mammal,FlyableMixIn):
#     pass
# dog=Dog()
# dog.run()
# bat=Bat()
# bat.fly()
# class student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return 'student object (name:%s)' % self.name
#     #__repr__=__str__
# # print(student('jsh'))
# s=student('jsh')
# print(s)
# class Fib(object):
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
# f = Fib()
# print(f[5])
# from enum import Enum
# Month=Enum('Month',('Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name,member in Month.__members__.items():
#     print(name,'==>',member,',',member.value)

# from enum import Enum,unique
# @unique
# class Weekday(Enum):
#     sun=0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# print(Weekday['Mon'])
# print(Weekday.Mon)
# from enum import  Enum,unique
# class Gender(Enum):
#     Male=0
#     Female=1
# class student(object):
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
# bart=student('Bart',Gender.Male)
# print(bart.name,bart.gender.value)
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         print('Error:', e)
#     finally:
#         print('finally...')
# main()
# class Dict(dict):
#     '''
#     Simple dict but also support access as x.y style.
#
#     >>> d1 = Dict()
#     >>> d1['x'] = 100
#     >>> d1.x
#     100
#     >>> d1.y = 200
#     >>> d1['y']
#     200
#     >>> d2 = Dict(a=1, b=2, c='3')
#     >>> d2.c
#     '3'
#     >>> d2['empty']
#     Traceback (most recent call last):
#         ...
#     KeyError: 'empty'
#     >>> d2.empty
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'Dict' object has no attribute 'empty'
#     '''
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
# if __name__=='__main__':
#     import doctest
#     doctest.testmod()
# import os
# print(os.path.abspath('.'))
# os.path.join('E:\Github\mypython\py36_practise','testdir')
# os.mkdir('E:\Github\mypython\py36_practise\estdir')

# import pickle
# # d=dict(name='bob',age=20,score=99)
# # with open('1.txt','wb') as f:
# #     pickle.dump(d, f) #序列化
# with open('1.txt','rb') as f:
#     print(pickle.load(f))
    #反序列化
    #f.write(pickle.dumps(d))
# print(pickle.dumps(d))
# import json
# d = dict(name='Bob', age=20, score=88)
# print(json.dumps(d))
# from multiprocessing  import Process
# import os
#
# def run_proc(name):
#      print('Run child process %s (%s)...' % (name,os.getpid()))
# if  __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('child process will start.')
#     p.start()
#     p.join()
#     print('child process end.')
# from multiprocessing import Pool
# import os,time,random
#
# def fact(n):
#  if n==1:
#   return 1
#  return n*fact(n-1)
#
# def long_time_task(name):
#     print('Run task %s (%s)...'%(name,os.getpid()))
#     start=time.time()
#     #time.sleep(random.random()*3)
#     print(fact(10))
#     end=time.time()
#     print('Task %s runs %0.2f seconds.'%(name,(end-start)))
#
# if __name__=='__main__':
#     print('Parent process %s.'% os.getpid())
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all subprocess done...')
#     p.close()
#     p.join()
#     print('All subprocess done.')
# from multiprocessing import  Pool
# import time
# import os
#
# def action1(a, b=50):
#     for i in range(b):
#         print(a, os.getpid(), ' ', i)  # os.getpid(): pid简单来说就是每个进程的“身份证”
#         time.sleep(0.1)
#
# if __name__ == '__main__':  # 还要添加这行，否则可能出现异常
#
#     ci = Pool(3)  # 创建一个进程池，容量为3个进程
#     ci.apply_async(action1, args=('进程一',))  # 启动第一个子进程...
#     ci.apply_async(action1, args=('进程二', 50))  # 和普通进程的启动方式有很大不同仔细看
#     ci.apply_async(action1, args=('进程三', 60))  # Pool的最基本格式记住←
# # 注意：程序现在有4个进程在运行：上面的三个子进程 和一个最为核心的：主进程
#
#     ci.close()  # 关闭进程池（但池子内已启动的子进程还会继续进行）
#     ci.join()  # 等待进程池内的所有子进程完毕
#     print('比如说这最后的一行输出就是主进程执行任务打印出来的')
# import multiprocessing
#
# def foo(aa):
#     ss = aa.get()  # 管子的另一端放在子进程这里，子进程接收到了数据
#     print('子进程已收到数据...')
#     print(ss)  # 子进程打印出了数据内容...
#
# if __name__ == '__main__':  # 要加这行...
#
#     tx = multiprocessing.Queue()  # 创建进程通信的Queue，你可以理解为我拿了个管子来...
#     jc = multiprocessing.Process(target=foo, args=(tx,))  # 创建子进程
#     jc.start()  # 启子子进程
#
#     print('主进程准备发送数据...')
#     tx.put('有内鬼，终止交易！')  # 将管子的一端放在主进程这里，主进程往管子里丢入数据↑
#     jc.join()
# from multiprocessing import Process,Queue
# import os,time,random
# #写数据进程执行的代码
# def  write(q):
#     print('Process to write %s.'%os.getpid())
#     for value in ['A','B','C']:
#         print('Put %s to queue...'%value)
#         q.put(value)
#         time.sleep(random.random())
# #读数据进程执行的代码：
# def read(q):
#     print('Process to read: %s...'% os.getpid())
#     while True:
#         value=q.get(True)
#         print('Get %s from queue.'% value)
#
# if __name__=='__main__':
#     #父进程创建Queue，并传给各个子进程：
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#     #启动子进程pw，写入
#     pw.start()
#     #启动子进程pr，读取
#     pr.start()
#     #等待pw结束
#     pw.join()
#     #pr进程里是死循环，无法等待其结束，只能强行终止
#     pr.terminate()
# import time,threading
# def loop():
#     print('thread %s is running...'% threading.current_thread().name)
#     n=0
#     while n<5:
#         n=n+1
#         print('thread %s >>>%s'%(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s ended.'% threading.current_thread().name)
# print('thread %s is running...'% threading.current_thread().name)
# t=threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended...'% threading.current_thread().name)
# import random, time, queue
# from multiprocessing.managers import BaseManager
#
# # 发送任务的队列:
# task_queue = queue.Queue()
# # 接收结果的队列:
# result_queue = queue.Queue()
#
# # 从BaseManager继承的QueueManager:
# class QueueManager(BaseManager):
#     pass
#
# # 自定义函数re_task_queue
# def re_task_queue():
#     global task_queue
#     return task_queue
#
# # 自定义函数re_result_queue
# def re_result_queue():
#     global result_queue
#     return result_queue
#
# if __name__ == '__main__':
#     # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
#     QueueManager.register('get_task_queue', callable=re_task_queue)
#     QueueManager.register('get_result_queue', callable=re_result_queue)
#     # 绑定端口5000, 设置验证码'abc':
#     manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
#     # 启动Queue:
#     manager.start()
#     # 获得通过网络访问的Queue对象:
#     task = manager.get_task_queue()
#     result = manager.get_result_queue()
#     # 放几个任务进去:
#     for i in range(10):
#         n = random.randint(0, 10000)
#         print('Put task %d...' % n)
#         task.put(n)
#     # 从result队列读取结果:
#     print('Try get results...')
#     for i in range(10):
#         r = result.get(timeout=10)
#         print('Result: %s' % r)
#     # 关闭:
#     manager.shutdown()
#     print('master exit.')
