from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User,Permission,Group

# 查找权限
from django.db.models import Q
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
            request.user.user_permissions.add(a_permission)
            if not request.user.has_perm('app.look_a_page'):
                return HttpResponse('当前用户没有权限访问该页面')
            else:
                return render(request,'a.html')

    def post(self,request):
        pass


class B(View):
    def get(self, request):
        # 判断用户当前是否登录  如果登录就添加相应权限
        if not request.user.is_authenticated:
            return render(request, 'place_login.html')
        else:
            # 获取指定用户---给他添加权限
            user = User.objects.get(username='test')

            # 创建和获取组
            # 表----用objects
            # get_or_create方法有则获取，无则创建  create单独使用重复创建会报错
            Group.objects.get_or_create(name='b_page_test')
            # get里面会有内置添加组add的方法，get_or_create没有，所以重复调用get方法
            group = Group.objects.get(name='b_page_test')

            # 获取content_type_id  为8的权限
            permissions = Permission.objects.filter(content_type_id=8)

            # 将id为8的权限添加到组
            for per in permissions:
                group.permissions.add(per)

            # 将用户添加到组
            user.groups.add(group)

            # 验证当前用户有没有自定义权限
            b_permisson = Permission.objects.filter(codename='look_b_page').first()
            # distinct()    权限去重
            users = User.objects.filter(Q(groups__permissions=b_permisson)|Q(user_permissions=b_permisson)).distinct()

            # 判断当前用户是否具有指定权限
            if request.user not in users:
                return HttpResponse('当前用户没有权限访问该页面')
            else:
                return render(request,'b.html')



    def post(self, request):
        pass