from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Userprofile,Group,Diary
from django.views.generic import View
# Create your views here.

class User_Data(View):
    def get(self,request):
        user = User()
        user.username = '正行'
        user.age = 18
        user.email = 'zhengxing@qq.com'
        user.phone = '1511112221'
        user.info = '阿坝阿坝'
        user.save()
        user.objects.create(username='马克',age=20,email='make@qq.com',phone='1301231144',info='嘻嘻嘻吧')
        return HttpResponse('successful')