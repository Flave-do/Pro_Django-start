from django.db import models

# Create your models here.
# 数据模型----基于类的
class Test(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)