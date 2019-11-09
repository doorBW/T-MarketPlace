from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import main.views

urlpatterns = [
    path('',  main.views.index, name='index'),
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
]
