from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Userprofile,Group,Diary
from django.views.generic import View

# 聚合查询
from django.db.models import Avg,Count,Sum
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
        # users = User.objects.filter(username='正行',id=1)
        # print(users)

        # 过滤附加条件查询  年龄大于19岁的
        # users = User.objects.all().exclude(age__gt=19)
        # print(users)

        # 模糊查询
        # users = User.objects.filter(username__contains='正')
        # print(users)

        # 查询userprofile
        # users = User.objects.all()[0]
        # user_profile = users.userprofile
        # print(user_profile)

        # 查询group
        # user = User.objects.all()[0]
        # groups = user.group
        # print(groups.values('name'))

        # 原生sql查询
        # users = User.objects.raw('select * from app_user')
        # print(users)

        # 反向查询
        # user = User.objects.filter(diary__id=1)
        # print(user)

        # 聚合查询
        user = User.objects.all().aggregate(Avg('age'))
        print(user)
        return HttpResponse('successful')