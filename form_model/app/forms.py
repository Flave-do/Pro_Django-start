from django import forms
from django.forms import fields
from .models import Auth

class AuthModelForm(forms.ModelForm):
    class Meta:
        # 绑定模型
        model = Auth

        # 渲染我们想要展示的模型字段
        fields = ['username','password']
        '''
        想要渲染出模型类的所有字段
        可以：
            fields = '__all__'
        
        '''
        # 定义不想渲染的字段
        # exclude = ['id']

        # 定义字段类型 一般情况下直接使用默认的转换类型 很少用
        fields_classes = {
            'username':forms.CharField,
            'password':forms.CharField
        }

        # 设置labe中文名称
        labels = {
            'username':'用户名',
            'password':'密码',
        }

        # 设置表单输入框显示的字符
        widgets = {
            'username':forms.TextInput(
                attrs={'placeholder':'请输入用户名'}
            ),
            'password':forms.PasswordInput(
                attrs={'placeholder':'请输入密码'}

            )
        }

        # 错误信息提示
        error_messages = {
            'username':{'required':'用户名不可为空'},
            'password':{'min_length':'密码长度不可小于十个字符'}

        }

    # 单项过滤
    def clean_username(self):
        username = self.cleaned_data.get('username','')  # 通过修改源代码输入空字符串，无默认值''会报错
        if len(username)>10:
            raise forms.ValidationError('用户名最大不可超过十个字符')
        return username
