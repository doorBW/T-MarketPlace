from django.db import models
from django.utils import timezone

# Create your models here.


class Market(models.Model):
    user = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
    url = models.TextField(null=True)
    content = models.TextField(null=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)


class Festival(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
    url = models.TextField(null=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
