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
        form = Auth(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username','')
            password = form.cleaned_data.get('password','')
            return HttpResponse('username is {},password is {}'.format(username,password))
        else:
            return render(request, 'register.html', {'form': form})