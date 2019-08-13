#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-8-13 19:52
# @Author : 江森辉
# @Site : 
# @File : 正方形螺旋线.py
# @Software: PyCharm
from turtle import *
setup(1000,800,100,50)
pensize(2)
pencolor("blue")
i=5
while (i<=480):
    seth(90)
    fd(i)
    seth(180)
    fd(i+5)
    seth(-90)
    fd(i+10)
    seth(0)
    fd(i+15)
    i=i+20
seth(90)
fd(485)
seth(180)
fd(490)
seth(-90)
fd(495)