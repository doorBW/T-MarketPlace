from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import main.views
from django.conf.urls.static import static
from django.conf import settings

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
    path('market/ajax/', main.views.market_click_ajax_event,
         name='market_click_ajax_event'),
    path('detail/festival/<int:pk>/update',
         main.views.festival_update, name='festival_update'),
    path('detail/market/<int:pk>/update',
         main.views.market_update, name='market_update'),
    path('auto_data_update', main.views.auto_market_data_saving,
         name='auto_market_data_saving')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
