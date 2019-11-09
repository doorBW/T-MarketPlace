from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/')
    files = models.FileField(upload_to='files/')
    upload_date = models.DateTimeField('Date published', default=timezone.now)

    def __str__(self):
        return self.user.username


class Market(models.Model):
    author = models.CharField(max_length=20,default="System")
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/',default='images/markets.png')
    address = models.CharField(max_length=1000)
    url = models.TextField(null=True)
    content = models.TextField(null=True)
    open_day = models.CharField(max_length=30,default="알 수 없음")
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)


class Festival(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    date = models.CharField(max_length=100)
    pay = models.CharField(max_length=50)
    host = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=1000)
    url = models.TextField(null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def summary(self):
        return self.content[:40]