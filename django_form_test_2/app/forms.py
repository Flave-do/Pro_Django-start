from django import forms
from django.forms import fields

class Auth(forms.Form):
    username = fields.CharField(
        # 限制用户输入的最大长度
        max_length=18,
        # 显示用户输入的最小长度
        min_length=4,
        label='用户名',
    )

    password = fields.CharField(
        widget=forms.PasswordInput(),
        label='密码',
        min_length=10,
    )

    # 全局认证
    def clean(self):
        username = self.cleaned_data.get('username','')
        password = self.cleaned_data.get('password','')

        if not username:
            raise forms.ValidationError('用户名不可为空')

        if len(username) > 10:
            raise forms.ValidationError('用户名不可超过十个字符')

        if not password:
            raise forms.ValidationError('密码不可为空')