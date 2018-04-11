# coding:utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# def index(request):
#     return HttpResponse(u"欢迎光临 自强学堂!")
def home(request):
    return render(request,'home.html')

#作为超链接功能
# def add(request):
#     return render(request,'add.html')

#作链接并传递参数c
# def add(request):
#     a=3
#     b=4
#     return render(request,'add.html',{'c':a+b})

#作链接并传递数组
# def add(requset):
#     TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
#     return  render(requset,'add.html',{'TutorialList':TutorialList})

#作链接并传递字典
# def add(request):
#     dict={'site':'自强学堂','content':'python.django'}
#     return render(request,'add.html',{'dict':dict})

#直接使用数据库
import pymssql
def dbaccess():
    conn = pymssql.connect(host='154.24.2.9', user='sa', password='sa!@#456', database='ESNT')
    cur = conn.cursor()
    cur.execute('select top 10 * from [ESNT].[dbo].[UDT$BLFMMAST_hall]')
    ret=cur.fetchall()
    conn.close()
    cur.close()
    return ret

def add(request):
    return render(request,'add.html',{'a':dbaccess()})

