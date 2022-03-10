from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(unique=True,max_length=20,blank=True)
    age = models.SmallIntegerField(default=0)
    phone = models.SmallIntegerField(db_index=True,blank=True,default=0)
    email = models.EmailField(blank=True,default='')
    info = models.TextField()
    crete_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    # 联合索引
    class Meta:
        index_together = ['username','phone']

    def __str__(self):
        return self.username


# 一对一表关系
class Userprofile(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.SET_NULL)
    birthday = models.CharField(max_length=50,blank=True,default='')

    def __str__(self):
        return 'user:{}.birthday:{}'.format(self.user,self.birthday)

# 一对多表关系
class Diary(models.Model):
    # related_name:可以在user表中通过diary查询相关用户打content信息
    user = models.ForeignKey(User,related_name='diary',on_delete=models.SET_NULL,blank=True,null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

# 多对多表关系
class Group(models.Model):
    user = models.ManyToManyField(User,related_name='group')
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)