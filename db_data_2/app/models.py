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

