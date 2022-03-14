from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import Auth
# Create your views here.

class Register(View):
    def get(self,request):
        form = Auth()
        return render(request,'register.html',{'form':form})


    def post(self,request):
        pass