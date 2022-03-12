import json
from functools import wraps
from django_redis import get_redis_connection
from django.db import models

# 缓存装饰器
_cache = get_redis_connection('default')
def cache(func):
    @wraps(func)        # 防止多次调用后装饰器后函数名被修改
    def wrapper(obj,*args):
        key = args[0]
        value = _cache.get(key)
        if value:
            return json.load(value)
        rs = func(obj,*args)
        _cache.set(key,json.dumps(rs))
        return rs
    return wrapper


# Create your models here.

class User(models.Model):
    username = models.CharField(unique=True,max_length=20,blank=True)
    age = models.SmallIntegerField(default=0)
    phone = models.CharField(max_length=11)
    email = models.EmailField(blank=True,default='')
    info = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    # 联合索引
    class Meta:
        index_together = ['username','phone']

    def __str__(self):
        return self.username

    @classmethod
    @cache
    def get(cls,id):
        rs = cls.objects.get(id=id)
        return {
            'id':rs.id,
            'username':rs.username,
            'age':rs.age,
            'info':rs.info,
            'create_time':str(rs.create_time),
            'update_time':str(rs.update_time),

        }