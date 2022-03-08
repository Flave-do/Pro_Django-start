from django.db import models

# Create your models here.
# 数据模型----基于类的
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    # uuique 唯一索引 该值不允许重复 该值不允许为空
    username = models.CharField(unique=True,max_length=20,blank=False)
    age = models.SmallIntegerField(default=0)
    phone = models.SmallIntegerField(db_column=True,blank=True,default=0)
    email = models.EmailField(blank=True,default='')
    info = models.TextField()

    # 创建时添加时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 更新时变更时间
    update_time = models.DateTimeField(auto_now=True)