from django.contrib import admin
from .models import Market, Festival, Profile

myModels = [Market, Festival, Profile]
admin.site.register(myModels)
