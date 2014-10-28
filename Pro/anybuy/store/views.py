#coding=utf-8

from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from system.models import *
import time

# Create your views here.
def helpcenter(request):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
    else:
        UserID = None
        UserType = None
        UserAccount = None
    return render_to_response('helpcenter.html', locals())

def getCommodity(request, cid):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
    else:
        UserID = None
        UserType = None
        UserAccount = None
    commodity = Commodity.objects.get(id=cid)
    shop = commodity.ShopID
    commentlist = Comment.objects.filter(CommodityID = cid)
    try:
        isfavorite = Favorite.objects.get(CommodityID = cid, CustomerID = UserID)
    except Favorite.DoesNotExist:
        isfavorite = False
    return render_to_response('Customer_CommodityInfo.html', locals())

def getShop(request, cid):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
    else:
        UserID = None
        UserType = None
        UserAccount = None
    shop = Shop.objects.get(id=cid)
    commodityList = Commodity.objects.filter(ShopID = shop)
    shopList = Shop.objects.filter(SellerID = shop.SellerID)
    return render_to_response('Customer_EnterShop.html', locals())

def favorite(request):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
    else:
        UserID = None
        UserType = None
        UserAccount = None
    favoriteList = Favorite.objects.filter(CustomerID = UserID)
    return render_to_response('Customer_Favorite.html', locals())

def cart(request):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
    else:
        UserID = None
        UserType = None
        UserAccount = None
    cartList = Cart.objects.filter(CustomerID = UserID)
    total=0
    for cart in cartList:
        total = total+cart.CartCommodityAmount*cart.CommodityID.SellPrice
    return render_to_response('Customer_MyCart.html', locals())

def add_to_cart(request, cid, amount, source):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
        user = Customer.objects.get(id=UserID)
        commodity = Commodity.objects.get(id = cid)
    else:
        UserID = None
        UserType = None
        UserAccount = None
    try:
        cart = Cart.objects.get(CustomerID = user, CommodityID = commodity)
        cart.CartCommodityAmount = cart.CartCommodityAmount+1
        cart.save()
    except Cart.DoesNotExist:
        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        Cart.objects.create(CartDate=date, CustomerID = user, CommodityID = commodity, CartCommodityAmount = int(amount))
    if source == 'commodity':
        return HttpResponseRedirect('/commodity/id/'+cid)
    else:
        return HttpResponseRedirect('/favorite/')
    #return render_to_response('Customer_CommodityInfo.html', locals())

def add_to_favorite(request):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
        user = Customer.objects.get(id=UserID)
    else:
        UserID = None
        UserType = None
        UserAccount = None
        user = None
    commodity = Commodity.objects.get(id = request.GET['id'])
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    Favorite.objects.create(FavoriteDate=date, CustomerID = user, CommodityID = commodity)
    return HttpResponse('You add: '+commodity.CommodityName)


def rm_from_cart(request):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
        user = Customer.objects.get(id=UserID)
    else:
        UserID = None
        UserType = None
        UserAccount = None
        user = None
    if 'id' in request.GET:
        commodity = Commodity.objects.get(id = request.GET['id'])
        Cart.objects.get(CustomerID = user, CommodityID = commodity).delete()
    else:
        commodity = None
    return HttpResponse('You removed: '+commodity.CommodityName)

def refreshcart(request):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
        user = Customer.objects.get(id=UserID)
    else:
        UserID = None
        UserType = None
        UserAccount = None
        user = None
    if 'id' in request.GET:
        commodity = Commodity.objects.get(id = request.GET['id'])
        cart = Cart.objects.get(CustomerID = user, CommodityID = commodity)
        cart.CartCommodityAmount = int(request.GET['amount'])
        cart.save()
    else:
        commodity = None
    return HttpResponse('You refresh: '+commodity.CommodityName)

def checkoutcart(request):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
        user = Customer.objects.get(id=UserID)
    else:
        UserID = None
        UserType = None
        UserAccount = None
        user = None
    date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    cutomerorder = CustomerOrder.objects.create(CustomerOrderState=0, CustomerOrderDate=date, CustomerID=user)
    # 从购物车中删除，现在是将checkbox注释了，所以这里是删除购物车中所有物品
    commoditylist = Cart.objects.filter(CustomerID=user)
    Cart.objects.filter(CustomerID = user).delete()
    for commodity in commoditylist:
        shoporder = ShopOrder.objects.create(ShopOrderState=0, ShopOrderDate=date, ShopID=commodity.ShopID)
        orderlist = OrderList.objects.create(CustomerOrderState=0, CustomerOrderDate=date, CustomerID=user, ShopID=commodity.ShopID, CommodityID = commodity)
        # 从购物车中删除，现在是将checkbox注释了，所以这里是删除购物车中所有物品
    return HttpResponse('You checked out your cart')

def rm_from_favorite(request):
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
        UserName = UserAccount
        user = Customer.objects.get(id=UserID)
    else:
        UserID = None
        UserType = None
        UserAccount = None
        user = None
    if 'id' in request.GET:
        commodity = Commodity.objects.get(id = request.GET['id'])
        Favorite.objects.get(CustomerID = user, CommodityID = commodity).delete()
    else:
        commodity = None
    return HttpResponse('You removed: '+commodity.CommodityName+'from favorite')


def search(request, keyword):  #/search/keyword/ 以keyword为关键字进行搜索，返回一个commodityList
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
    else:
        UserID = None
        UserType = None
        UserAccount = None
    commodityList = Commodity.objects.filter(CommodityName__contains = keyword)
    commodityList_by_amount = commodityList.order_by('SoldAmount')
    commodityList_by_price = commodityList.order_by('SellPrice')
    commodityList_by_counterprice = commodityList.order_by('-SellPrice')
    return render_to_response('Customer_CommodityList.html', locals())

def sellerhome(request): #需要返回shoplist，shopadvlist，commodityadvlist
    if request.session.get('UserID', False):
        UserID = request.session['UserID']
        UserType = request.session['UserType']
        UserAccount = request.session['UserAccount']
    else:
        return HttpResponseRedirect('/login/')
    seller = Seller.objects.get(id=UserID)
    shoplist = Shop.objects.filter(SellerID = seller)
    shopadvlist = ShopAdv.objects.filter(OwnerID = seller)
    commodityadvlist = CommodityAdv.objects.filter(OwnerID = seller)
    return render_to_response('Customer_CommodityList.html', locals())
