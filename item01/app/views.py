from django.shortcuts import render
from django.views.generic import View
from .consts import MessageType

# Create your views here.
class Message(View):
    def get(self,request,message_type):
        data = {}
        try:
            message_type_obj = MessageType[message_type]
        except:
            data['error'] = '没有这个消息类型'
            render(request,'message.html',data)

        message = request.GET.get('message','')
        if not message:
            data['error'] = '消息不可为空'
            return render(request,'message.html',data)

        data['message'] = message
        data['message_type'] = message_type_obj
        return render(request, 'message.html', data)