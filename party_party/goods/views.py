from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Goods, SemiGoods,Like,semiLike



def goodslist(request) :
    product = Goods.objects.all()
    return render(request, 'goods_list.html')

def goodsdetail(request, product_id) :
    product = Goods.objects.get(id = product_id)
    return render(request, 'goods_detail.html', {'product' : product})


def write_choices(request):
    return render(request, 'write_choices.html')

def semi_goods(request) : #수요조사폼이 글작성
    return render(request, 'write_semigoods.html')


def semiproduct(request, semi_goods_id):
    new_semigoods = SemiGoods.objects.get(id = semi_goods_id)
    try:
        liked =  new_semigoods.like.filter(user = request.user).exists()
    except:
        liked = False
    total_likes = new_semigoods.like.all()
    count = 0
    for l in total_likes:
        count +=1
    return render(request, "goods_detail.html")


def create_semi(request):
    #if not request.session.get('user'):

    #return redirect('/users/login')


    if(request.method == 'POST'):
        new_semigoods=SemiGoods()

        new_semigoods.product = request.POST['product']
        new_semigoods.image = request.FILES['product_imgs']
        new_semigoods.price=request.POST['semi_price']
        new_semigoods.count=request.POST['semi_count'] 
        new_semigoods.tag = request.POST['tag']


        new_semigoods.writer = request.user
        new_semigoods.pud_date = timezone.now()

        new_semigoods.email=request.POST['email']
        new_semigoods.twitter=request.POST['twitter']
        
        new_semigoods.information_needs=request.POST['information']
        
            
        new_semigoods.save()
    return redirect('semiproduct', new_semigoods.id)

def goods(request): #입금폼 작성
    goods = Goods.object.all()
    return render(request, 'write_goods.html')




def mypage(request):
    return render(request, 'mypage.html')


def mypartiform(request):
    return render(request, 'mypartiform.html')


def myinfo(request):
    return render(request, 'myinfo.html')


def myfavp(request):
    return render(request, 'myfavp.html')



def myfavw(request):
    return render(request, 'myfavw.html')

def mytag(request):
    return render(request, 'mytag.html')


def mywriting(request):
    return render(request, 'mywriting.html')
