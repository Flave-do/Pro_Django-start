from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User,Permission,Group
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
        password = request.POST.get('password','')
        check_password = request.POST.get('check_password','')
        if password != check_password:
            return HttpResponse('密码输入不一致')

        # 判断当前注册帐号是否已注册，如果已经被注册则提示已注册
        exists = User.objects.filter(username=username).exists()
        if exists:
            return HttpResponse('该帐号已被注册 请重新注册')
        User.objects.create_user(username=username,password=password)
        return redirect(reverse('login'))


# 登录
class Login(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        # 判断当前用户是否存在，如果不存在则让用户重新注册
        exists = User.objects.filter(username=username).exists()
        if not exists:
            return HttpResponse('该帐号不存在 请注册')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect(reverse('index'))
        else:
            return HttpResponse('密码错误')


# 网站首页
class Index(View):
    def get(self, request):
        return render(request,'index.html')

    def post(self, request):
        pass


# 注销
class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('register'))


# 基于类的验证  针对单个用户
class A(View):
    def get(self,request):
        # 判断用户当前是否登录
        if not request.user.is_authenticated:
            return render(request,'place_login.html')
        else:
            a_permission = Permission.objects.get(codename='look_a_page')
            # 添加权限
            request.user.user.has_permissions.add(a_permission)
            if not request.user.has_perm('app.look_a_page'):
                return render(request,'a.html',{'error':'当前用户没有权限访问该页面'})
            else:
                return render(request,'a.html')

    def post(self,request):
        pass


class B(View):
    def get(self, request):
        pass

    def post(self, request):
        pass