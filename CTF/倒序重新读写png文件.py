# coding:utf-8
# author:Reborn

f1 = open('flag.png','rb+')
f2 = open('fla.png','wb+')
f2.write(f1.read()[::-1])
f1.close()
f2.close()

