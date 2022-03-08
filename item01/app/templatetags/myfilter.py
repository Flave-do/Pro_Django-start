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

@register.filter(name='deep_check_message')
def deep_check(value):
    cut_message = jieba.lcut(value)
    new_message = []
    for m in cut_message:
        if m in SenstiveWord:
            new_message.append('*')
        else:
            new_message.append(m)


    if new_message:
        return ''.join(new_message)
    return value