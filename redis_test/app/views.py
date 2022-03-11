from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.views.generic import View

# Create your views here.

class UserInfo(View):
    def get(self,request):
        user = User()
        user.username = '山河'
        user.age = 20
        user.email = 'shanhe@sina.com'
        user.info = '此人很懒，什么也没有留下'
        user.save()
        return HttpResponse('successful')