from django.contrib import admin
from django.urls.conf import include
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('goodslist/', goodslist, name = "goodslist"),
    path('goodsdetail/<str:product_id>', Semigoodsdetail, name = "goodsdetail"),
    path('write_semigoods/', write_semigoods, name = "write_semigoods"),
    path('create_semi/', create_semi,name='create_semi'),
    path('write_goods/', write_goods, name = "write_goods"),
    # path('create/', create,name='create'),
    path('write_choices/',write_choices,name="write_choices"),
    path('mypage/', mypage, name='mypage'),
    path('myfavp/',myfavp,name='myfavp'),
    path('myfavw/',myfavw,name='myfavw'),
    path('myinfo/',myinfo,name='myinfo'),
    path('mypartiform/',mypartiform,name='mypartiform'),
    path('mytag/',mytag,name='mytag'),
    path('mywriting/',mywriting,name='mywriting'),
    path('needform/', needform, name = "needform"),
    path('depoform/', depoform, name = 'depoform'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
