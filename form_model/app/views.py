from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import AuthModelForm
from .models import Auth

# Create your views here.
class Register(View):
    def get(self,request):
        user = Auth.objects.filter(pk=1).first()
        if user:
            form = AuthModelForm(instance=user)
        else:
            form = AuthModelForm()

        return render(request,'register.html',{'form':form})

    def post(self,request):
        form = AuthModelForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username','')
            password = form.cleaned_data.get('password', '')
            form.save()
            return HttpResponse('username is {},password is {}'.format(username,password))
        else:
            return render(request, 'register.html', {'form': form})