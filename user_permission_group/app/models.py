from django.db import models

# Create your models here.

class Apage(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return 'title:{}'.format(self.title)

    class Meta:
        permissions = [
            ('look_a_page','can get this a page message')
        ]


class Bpage(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return 'title:{}'.format(self.title)

    class Meta:
        permissions = [
            ('look_b_page','can get this a page message')
        ]