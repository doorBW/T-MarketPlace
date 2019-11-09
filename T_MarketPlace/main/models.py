from django.db import models
from django.utils import timezone

# Create your models here.


class Market(models.Model):
    user = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


class Festival(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
