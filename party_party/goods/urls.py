from django.contrib import admin
from django.urls.conf import include
from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("goodslist/", goodslist, name="goodslist"),
    path("goodsdetail/<str:product_id>", product, name="goodsdetail"),
    path("write_semigoods/", semi_goods, name="write_semigoods"),
    path("create_semi/", create_semi, name="create_semi"),
    path("write_goods/", goods, name="write_goods"),
    # path('create/', create, name='create'),
    path("write_choices/", write_choices, name="write_choices"),
    path("mypage/", mypage, name="mypage"),
    path("myfavp/", myfavp, name="myfavp"),
    path("myfavw/", myfavw, name="myfavw"),
    path("myinfo/", myinfo, name="myinfo"),
    path("mypartiform/", mypartiform, name="mypartiform"),
    path("mytag/", mytag, name="mytag"),
    path("mywriting/", mywriting, name="mywriting"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
