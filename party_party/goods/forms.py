from django import forms
from .models import SemiGoods,Goods




class semigoodsForm(forms.Form):
    product = forms.CharField(error_messages = {'required':"상품 이름을 입력해주세요"},label = "product",max_length = 30)
    product_image = models.ImageField(error_messages = {'required':"상품 도안을 입력해주세요"},label = "product_image",upload_to="semigoods/")
    
    semi_price = models.IntegerField(
        error_messages={'required': "예상가격을 입력해주세요"}, label="semi_price")
    semi_count = models.IntegerField(
        error_messages={'required': "예상수량을 입력해주세요"}, label="semi_count")
    tag = models.CharField(error_messages = {'required':"상품 분류를 선택해주세요"}, label = "tag",max_length=80)
    end_date=models.DateField(label="end_date")
    email=models.EmailField(help_text='이메일을 입력해주세요(선택)',null=True,max_length = 200)
    twitter=models.CharField(error_messages = {'required':"트위터 계정을을 입력해주세요"}, label = "twitter",max_length=20)
    information_needs = models.CharField(error_messages = {'required':"상품 설명을 입력해주세요"}, label = "info",max_length=500)
    
