from django.shortcuts import render
from .mongo_engine import Users,Paper
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

class Mongo_User(View):
    def get(self,request):
        user = Users.objects.create(name='shanhe',age=20)
        return HttpResponse('my name is {},age is {}'.format(user.name,user.age))
    