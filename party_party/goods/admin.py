from django.contrib import admin
from .models import SemiGoods,Goods,User




class BoardAdmin(admin.ModelAdmin):
    list_display = ('product', 'product_image','writer', )

admin.site.register(SemiGoods, BoardAdmin)