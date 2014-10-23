#coding=utf-8

from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from system.models import *

# Create your views here.
def getCommodity(request, cid):
	if request.session['UserID']:
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
	return render_to_response('Customer_CommodityInfo.html', locals())

def getShop(request, cid):
	if request.session['UserID']:
		UserID = request.session['UserID']
		UserType = request.session['UserType']
		UserAccount = request.session['UserAccount']
		UserName = UserAccount
	else:
		UserID = None
		UserType = None
		UserAccount = None

def search(request, keyword):  #/search/keyword/ 以keyword为关键字进行搜索，返回一个commodityList
	if request.session['UserID']:
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
	return render_to_response('Customer_CommidityList.html', locals())
