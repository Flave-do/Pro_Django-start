from django import forms
from django.forms import fields

class Auth(forms.Form):
    username = fields.CharField(
        # 限制用户输入的最大长度
        max_length=10,
        # 显示用户输入的最小长度
        min_length=4,
        label='用户名',
    )

    password = fields.CharField(
        widget=forms.PasswordInput(),
        label='密码',
        min_length=10,
    )