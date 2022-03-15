from django.shortcuts import render,reverse,redirect
from django.views.generic import View

# 直接在页面显示相应的错误
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.

# 注册
class Register(View):
    def get(self,request):
        # 判断用户当期是否登录，如果登录直接跳转到主页
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        return render(request,'register.html')

    def post(self,request):
        username = request.POST.get('username','')


# 登录
class Login(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 网站首页
class Index(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 注销
class LogoutUser(View):
    def get(self, request):
        pass

    def post(self, request):
        pass