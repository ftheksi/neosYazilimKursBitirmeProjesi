from django.shortcuts import render, get_object_or_404, redirect
from .models import *
import random
from random import randint
# Create your views here.

def basketCount(request):
    if request.user.is_authenticated:
        return Shopbasket.objects.filter(user=request.user)
    else:
        return None


def homePage(request):
    urunler = list(Urunler.objects.all())
    urunler = random.sample(urunler, 8)

    context={
        "shopbasket":basketCount(request),
        "urunler":urunler,
    }
    return render(request,'homepage.html',context)

def iletisim(request):
    context={
        "shopbasket":basketCount(request),
    }
    return render(request,'iletisim.html',context)

def urunler(request):
    urunler=UrunStok.objects.all()
    context={
        "shopbasket":basketCount(request),
        "urunler":urunler,
    }
    return render(request,'urunler.html',context)

def urunDetay(request,slug):
    urun = get_object_or_404(UrunStok, urun__slug=slug)
    prdct=Urunler.objects.get(slug=slug)
    comments=Comment.objects.filter(product=prdct).order_by("-star")
    puan=0
    if request.method=="POST":
        submit=request.POST.get("submit")
        if submit=="buy":
            size=request.POST.get("size")
            count=int(request.POST.get("count"))
            prod=BedenKiyafet.objects.filter(beden__title=size,urun__title=urun).get()
            price_all=prod.fiyat * count
            shopprod=Shopbasket.objects.filter(user=request.user,product_letter=prod)
            if shopprod.exists():
                shopprod=shopprod.get()
                shopprod.count+=count
                shopprod.price_all+=price_all
                shopprod.save()
            else:
                shopb=Shopbasket(user=request.user,product_letter=prod,price_all=price_all,count=count)
                shopb.save()
            return redirect('/urun-detay/'+slug+'/')
        elif submit=="comment":
            text=request.POST.get("text")
            try:
                star=int(request.POST.get("star"))
            except:
                return redirect('/urun-detay/'+slug+'/')
            
            comment=Comment(text=text,star=star,user=request.user,product=prdct)
            comment.save()

            print("TOPLAM YORUM SAYISI",len(comments))
            for i in comments:
                puan+=i.star
            print("PUAN",puan)

            prdct.puan=round(puan/len(comments),1)
            prdct.save()
            
            return redirect('/urun-detay/'+slug+'/')
            

    listprice=[]
    listsize=[]
    sizeprice=urun.beden_kiyafet.all()
    for i in range(len(sizeprice)):
        listprice.append(sizeprice[i].fiyat)
        listsize.append(sizeprice[i].beden.slug)

    context={
        "shopbasket":basketCount(request),
        "urun":urun,
        "listprice": listprice,
        "listsize": listsize,
        "comments":comments
    }
    return render(request,'urun-detay.html',context)

def ShopBasket(request):

    shopbasket=Shopbasket.objects.filter(user=request.user)
    total=0
    for i in shopbasket:
        total+=i.price_all
    
    if request.method=="POST":
        for k,v in dict(request.POST).items():
            if k !="csrfmiddlewaretoken":
                shopb=shopbasket.get(id=k[5:])
                if v[0]=="0":
                    shopb.delete()
                else:
                    shopb.count=v[0]
                    shopb.price_all=shopb.product_letter.fiyat * int(v[0])
                    shopb.save()
                
        return redirect('ShopBasket')
    

    context={
        "shopbasket":Shopbasket.objects.filter(user=request.user),
        "total":total,
    }
    return render(request,'user/sepet.html',context)

def ShopBasketDelete(request,sid):

    shopbasket=Shopbasket.objects.get(id=sid)
    shopbasket.delete()


    return redirect('ShopBasket')
