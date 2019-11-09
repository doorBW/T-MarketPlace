from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import main.views

urlpatterns = [
    path('',  main.views.index, name='index'),
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
    path('detail/market/<int:market_id>/',
         main.views.market_detail, name='market_detail'),
    path('detail/festival/<int:festival_id>/',
         main.views.festival_detail, name='festival_detail'),
    path('market/new/', main.views.market_new, name='market_new'),
    path('festival/new/', main.views.festival_new, name='festival_new'),
]
