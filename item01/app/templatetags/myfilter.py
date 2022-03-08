from django import template
from app.consts import SenstiveWord

import jieba

register = template.Library()
@register.filter
def simple_check(value):
    cut_message = jieba.lcut(value)
    check = list(set(cut_message) & set(SenstiveWord))
    print(cut_message)
    if check:
        return '该消息涉及敏感关键字,已被屏蔽'
    return value