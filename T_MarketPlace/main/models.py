from django.db import models
from django.utils import timezone

# Create your models here.

class Market(models.Model):
    author = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=1000)
    url = models.TextField(null=True)
    content = models.TextField(null=True)
    open_day = models.CharField(max_length=30)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)


class Festival(models.Model):
    market = models.ForeignKey(Market, on_delete = models.CASCADE)
    name = models.CharField(max_length=20)
    date = models.CharField(max_length=100)
    pay = models.CharField(max_length=50)
    host = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    address = models.CharField(max_length=1000)
    url = models.TextField(null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
