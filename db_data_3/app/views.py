from django.shortcuts import render

# Create your views here.
from .models import User
from django.views.generic import View

class UserInfo(View):
    def get(self,request):
        # 创建数据
        User.objects.create(username='正行',age=20)
        user = User(username='马克',age=18)
        user.save()
        return render(request,'UserInfo.html')