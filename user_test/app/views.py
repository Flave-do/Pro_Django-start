from django.shortcuts import render
from django.views.generic import View
# Create your views here.

# 注册
class Register(View):
    def get(self,request):
        pass

    def post(self,request):
        pass


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