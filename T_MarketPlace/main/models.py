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
    user = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


class Festival(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
