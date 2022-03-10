from django.shortcuts import render

# Create your views here.
from .models import User
from django.views.generic import View

class UserInfo(View):
    def get(self,request):
        # 创建数据
        # User.objects.create(username='正行',age=20)

        # user = User(username='马克',age=18)
        # user.save()

        # user = User()
        # user.username = '山河'
        # user.age = 21
        # user.save()

        # 查询方法
        # user = User.objects.get(id=1)
        # Users = User.objects.all()
        # print(Users)

        # user = User.objects.get_or_create(username='么可')
        # print(user)

        # 更新方法
        user = User.objects.filter(id=1).update(age=25)
        
        return render(request,'UserInfo.html')