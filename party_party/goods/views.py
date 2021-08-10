from django.shortcuts import render, redirect
from .models import *

def goodslist(request) :
    product = Goods.objects.all()
    return render(request, 'goods_list.html')

def product(request, product_id) :
    products = Goods.object.get(id = product_id)
    return render(request, 'goods_detail.html', {'products' : products})


def write_choices(request):
    return render(request, 'write_choices.html')

def semi_goods(request) : #수요조사폼이 글작성
    '''
    if(request.method == 'POST'):
        new_idea = SemiGoods()
        new_idea.product = request.POST['title']
        new_idea.product_image =request.
        new_idea.writer = request.user
        new_idea.pud_date = timezone.now()

        new_idea.email=request.POST['email']
        new_idea.twitter=request.POST['twitter']
        new_idea.item = request.POST['item']

        if not request.FILES:
            new_idea.image = ""
            new_idea.save()

        else:
            new_idea.image = request.FILES['image']
            new_idea.save()
'''
    semigoods = SemiGoods.object.all() 
    return redirect(request,'write_semi_goods.html')


def goods(request): #입금폼 작성
    goods = Goods.object.all()
    return render(request, 'write_goods.html')

'''
def create_semi(request):
    if(request.method == 'POST'):
        new_idea.product = request.POST['title']
        new_idea.writer = request.user
        new_idea.pud_date = timezone.now()

        new_idea.email=request.POST['email']
        new_idea.twitter=request.POST['twitter']
        new_idea.item = request.POST['item']

        if not request.FILES:
            new_idea.image = ""
            new_idea.save()

        else:
            new_idea.image = request.FILES['image']
            new_idea.save()

    return redirect('detail', new_idea.id)
'''