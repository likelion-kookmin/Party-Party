from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField, DateField
from django.forms.fields import ImageField
User = get_user_model()



# Create your models here.


class Goods(models.Model):

    product = models.CharField(max_length=20)
    product_image = models.ImageField(
        default="../static/daytoyear.jpg", blank=True, upload_to="images/", null=True)
    writer = models.ForeignKey(User, on_delete = CASCADE, related_name = "regist")
    price = models.IntegerField()
    count = models.IntegerField()
    tag = models.CharField(max_length=80, default='그 외')
    start_date = models.DateField(db_column='Start Date')
    end_date = models.DateField(db_column='End Date')  # 마감일

    bank_deposit = models.CharField(max_length=50,default="분류")
    account_deposit = models.IntegerField()
    account_owner =models.CharField(max_length=30,default="예금주 이름을 입력하세요")
    howto_delivery = models.CharField(max_length=10)

    email = models.EmailField(null=True, max_length=200)
    twitter = models.CharField(max_length=20)
    information_needs = models.CharField(max_length=500)
    

    
    

    def __str__(self):
        return self.product


class SemiGoods(models.Model):

    product = models.CharField(max_length=30)
    product_image = models.ImageField(
        default="../static/daytoyear.jpg", blank=True, upload_to="images/", null=True)

    writer = models.ForeignKey(User, on_delete=CASCADE, related_name="semiregist")
    semi_price = models.IntegerField(default=0)
    semi_count = models.IntegerField(default=0)
    tag = models.CharField(max_length=80, default='그 외')
    end_date = models.DateField(null=True)

    email = models.EmailField(null=True, max_length=200)
    twitter = models.CharField(max_length=20)
    information_needs = models.CharField(max_length=500)

    def __str__(self):
        return self.product


class SemiPhoto(models.Model):
    post = models.ForeignKey(SemiGoods, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


class semiLike(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="semi_like")
    semigoods = models.ForeignKey(
        SemiGoods, on_delete=CASCADE, related_name="semi_like")


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="like")
    goods = models.ForeignKey(Goods, on_delete=CASCADE, related_name="like")
