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

    def post(self, request):
        pass