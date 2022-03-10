from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Userprofile,Group,Diary
from django.views.generic import View
# Create your views here.

class User_Data(View):
    def get(self,request):
        # user = User()
        # user.username = '正新'
        # user.age = 18
        # user.email = 'zhengxing@qq.com'
        # user.phone = '1511112221'
        # user.info = '阿坝阿坝'
        # user.save()
        # User.objects.create(username='马克',age=20,email='make@qq.com',phone='1301231144',info='嘻嘻嘻吧')

        # user = User.objects.get(id=1)
        # user_profile = Userprofile()
        # user_profile.user = user
        # user_profile.birthday = '1995-11-25'
        # user_profile.save()
        #
        # diary = Diary()
        # diary.user = user
        # diary.content = '正行老斯，我们一起学怕从'
        # diary.save()
        #
        # group = Group()
        # group.name = '开发'
        # group.save()
        # group.user.add(user)

        # 查询
        # zhengxing = User.objects.get(pk=1)
        # data = zhengxing.diary.values('content')
        # print(data)

        # 集合查询
        # users = User.objects.all()
        # print(list(users))

        #过滤查询
        users = User.objects.filter(username='正行',id=1)
        print(users)
        return HttpResponse('successful')