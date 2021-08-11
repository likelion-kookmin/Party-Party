from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Goods, SemiGoods,Like,semiLike



def goodslist(request) :
    product = Goods.objects.all()
    return render(request, 'goods_list.html')

def goodsdetail(request, product_id) :
    product = SemiGoods.objects.get(id = product_id)
    return render(request, 'goods_detail.html', {'product' : product})


def write_choices(request):
    return render(request, 'write_choices.html')



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

def write_semigoods(request) : #수요조사폼에 글작성
    return render(request, 'write_semigoods.html')

def create_semi(request): # 데이터 값을 넘기는 함수
    #if not request.session.get('user'):

    #return redirect('/users/login')


    if(request.method == 'POST'):
        new_semigoods=SemiGoods()

        new_semigoods.product = request.POST['product']
        new_semigoods.image = request.FILES['product_image']
        new_semigoods.price=request.POST['semi_price']
        new_semigoods.count=request.POST['semi_count'] 
        new_semigoods.tag = request.POST['tag']


        new_semigoods.writer = request.user
        new_semigoods.pud_date = timezone.now()

        new_semigoods.email=request.POST['email']
        new_semigoods.twitter=request.POST['twitter']
        
        new_semigoods.information_needs=request.POST['information_needs']
        
        
        new_semigoods.save()    
        
    return redirect('goodsdetail', new_semigoods.id)

def write_goods(request): #입금폼 작성
    goods = Goods.object.all()
    return render(request, 'write_goods.html')

def success(request):
    return HttpResponse('successfully uploaded')


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
