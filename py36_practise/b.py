# def fact(n):
#  if n==1:
#   return 1
#  return n*fact(n-1)
#
# print(fact(120))
# task_worker.py

# import time, sys, queue
# from multiprocessing.managers import BaseManager
#
# # 创建类似的QueueManager:
# class QueueManager(BaseManager):
#     pass
#
# # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
# QueueManager.register('get_task_queue')
# QueueManager.register('get_result_queue')
#
# # 连接到服务器，也就是运行task_master.py的机器:
# server_addr = '127.0.0.1'
# print('Connect to server %s...' % server_addr)
# # 端口和验证码注意保持与task_master.py设置的完全一致:
# m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# # 从网络连接:
# m.connect()
# # 获取Queue的对象:
# task = m.get_task_queue()
# result = m.get_result_queue()
# # 从task队列取任务,并把结果写入result队列:
# for i in range(10):
#     try:
#         n = task.get(timeout=1)
#         print('run task %d * %d...' % (n, n))
#         r = '%d * %d = %d' % (n, n, n*n)
#         time.sleep(1)
#         result.put(r)
#     except Queue.Empty:
#         print('task queue is empty.')
# # 处理结束:
# print('worker exit.')
import sympy   # 引入解方程的专业模块sympy2 3
x,y = sympy.symbols("x y")   # 申明未知数"x"和"y"4
a = sympy.solve([3*x -2*y-3,x+2*y-5],[x,y])   # 写入需要解的方程组5 print(a)  # 打印出结果
print(a)