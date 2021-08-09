from django.contrib import admin
from django.urls.conf import include
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('goods_detail/', goods_detail, name = "detail"),
    path('write_semigoods/', semi_goods, name = "write_semigoods"),
    path('write_goods/', goods, name = "write_goods"),
    path('write_choices/',write_choices,name="write_choices"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)