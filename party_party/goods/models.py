from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField

User = get_user_model()


ITEM_CHOICES= {
      ('2D','2D'), #오른쪽에 있는 것이 화면에 보인다.
      ('people', '실존인물'),
      ('character', '캐릭터'),
      ('etc','그외')
  }

# Create your models here.
class Goods(models.Model) :
    
    product = models.CharField(max_length = 20)
    product_image = models.ImageField(upload_to="goods/")
    writer = models.ForeignKey(User, on_delete = CASCADE, related_name = "regist")
    price = models.IntegerField()
    count = models.IntegerField()
    item = models.CharField(max_length=80, choices=ITEM_CHOICES)  #상품 분류
    end_date=models.DateField(db_column='End Date') #마감일
    term_needs = models.DateField()
    term_deposit = models.IntegerField()
    information_needs = models.CharField(max_length=500)
    information_deposit = models.CharField(max_length=500)
    account_deposit = models.CharField(max_length= 50)
    count_needs = models.IntegerField()
    count_deposit = models.IntegerField()

    howto_delivery = models.CharField(max_length=10)
    location1 = models.CharField(max_length=20)
    location2 = models.CharField(max_length=20)
    zip_code = IntegerField()


    def __str__(self):
        return self.product


class SemiGoods(models.Model):

    product = models.CharField(max_length = 30)
    product_image = models.ImageField(upload_to="semigoods/")
    
    writer = models.ForeignKey(User, on_delete = CASCADE, related_name = "semiregist")
    semi_price = models.IntegerField()
    semi_count = models.IntegerField()
    tag = models.CharField(max_length=80,null = True)

    email=models.EmailField(null=True,max_length = 200)
    twitter=models.CharField(max_length=20)
    information_needs = models.CharField(max_length=500)
    
    def __str__(self):
        return self.product





class semiLike(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE, related_name= "semi_like")
    semigoods = models.ForeignKey(SemiGoods,on_delete=CASCADE, related_name= "semi_like")


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE, related_name= "like")
    goods = models.ForeignKey(Goods,on_delete=CASCADE, related_name= "like")


