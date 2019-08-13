#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-8-13 19:49
# @Author : 江森辉
# @Site : 
# @File : 乘法口诀.py
# @Software: PyCharm
print("\n".join("\t".join(["%s*%s=%s" % (y, x, x * y)for y in range(1, x + 1)]) for x in range(1, 10)))