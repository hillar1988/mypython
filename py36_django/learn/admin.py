#from django.contrib import admin

# Register your models here.
#加入下面三句话，就能拥有一个后台
from django.contrib import admin
from .models import Stu

admin.site.register(Stu)