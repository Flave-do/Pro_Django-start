from django.db import models

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