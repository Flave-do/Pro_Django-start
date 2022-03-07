from .base_render import render_to_response
from django.views.generic import View


# Create your views here.

class Index(View):
    def get(self,request):
        data = {'name':'zhengxin','age':20}
        return render_to_response(request,'index.html',data=data)

