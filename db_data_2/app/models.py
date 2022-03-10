from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True,max_length=20,blank=True)
    age = models.SmallIntegerField(default=0)
    phone = models.SmallIntegerField(db_index=True,blank=True,default=0)
    email = models.EmailField(blank=True,default='')
    info = models.TextField()
    crete_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

# 一对一表关系
class Userprofile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.SET_NULL)
    brithday = models.CharField(max_length=50,blank=True,default='')

# 一对多表关系
class Userlog(models.Model):
    id =models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,related_name='user_log',on_delete=models.SET_NULL,blank=True,null=True)
    content = models.TextField()
    create_time = models.DateTimeField()

# 多对多表关系
class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ManyToManyField(User,related_name='group')
    name = models.CharField(max_length=20)
    create_time = models.IntegerField(default=0)