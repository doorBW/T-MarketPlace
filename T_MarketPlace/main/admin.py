from django.contrib import admin
from .models import Market, Festival

myModels = [Market, Festival]
admin.site.register(myModels)
