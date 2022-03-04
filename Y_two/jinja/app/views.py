from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import View

class Index(View):
    def get(self,request):
        data = {'name':'zhengxing','age':19}
        return render(request,'index.html',data)