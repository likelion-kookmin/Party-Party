from django.contrib import admin
from django.urls.conf import include
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('goodslist/', goodslist, name = "goodslist"),
    path('goodsdetail/<str:product_id>', product, name = "goodsdetail"),
    path('write_semigoods/', semi_goods, name = "write_semigoods"),
    path('write_goods/', goods, name = "write_goods"),
    path('write_choices/',write_choices,name="write_choices"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)