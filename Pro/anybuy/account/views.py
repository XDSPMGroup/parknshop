# Create your views here.
    #coding=utf-8
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from system.models import *
import hashlib
import datetime

#定义表单模型
IDENTITY = (
('C', 'Customer'),
('S', 'Seller'),
)

class CustomerForm(forms.Form):
	identity = forms.ChoiceField(label='Identity:', choices=IDENTITY)
	CustomerAccount = forms.CharField(label='Account :', max_length=64)
	CustomerName = forms.CharField(label='Realname:', max_length=64)
	CustomerPassword = forms.CharField(label='Password:', widget=forms.PasswordInput(), max_length=16)
	#CustomerType = forms.CharField(label='Type：', max_length=1, choices=CustomerTypeChoices,blank=True)
	CustomerTelephone = forms.CharField(label='Telephone:',max_length=64)
	CustomerEmail = forms.EmailField(label='Emailaddr:')
	CustomerAddress = forms.CharField(label='RealAddr :')

class CustomerForm2(forms.Form):
	#identity = forms.ChoiceField(label='your identity:', choices=IDENTITY)
	CustomerAccount = forms.CharField(label='Account:', max_length=64)
	CustomerName = forms.CharField(label='YourName:', max_length=64)
	CustomerPassword = forms.CharField(label='Password:', widget=forms.PasswordInput(), max_length=16)
	#CustomerType = forms.CharField(label='Type：', max_length=1, choices=CustomerTypeChoices,blank=True)
	CustomerTelephone = forms.CharField(label='Phone:',max_length=64)
	CustomerEmail = forms.EmailField(label=   'E-mail:')
	CustomerAddress = forms.CharField(label=  'Address:')

class UserForm(forms.Form):
	identity = forms.ChoiceField(label=  'identity:', choices=IDENTITY)
	UserAccount = forms.CharField(label= 'Account: ', max_length=64)
	UserPassword = forms.CharField(label='Password:', widget=forms.PasswordInput(), max_length=16)

# Create your views here.

def register(request):
	duplicate=False
	if request.method == "POST":
		cf = CustomerForm(request.POST)
		if cf.is_valid():
			#get form
			if cf.cleaned_data['identity'] == 'C':
				customer = Customer()
				customer.CustomerAccount = cf.cleaned_data['CustomerAccount']
				cu=Customer.objects.filter(CustomerAccount=customer.CustomerAccount)
				if len(cu) == 1:
					duplicate=True
					return render_to_response('register.html',locals(), context_instance=RequestContext(request))
				customer.CustomerName = cf.cleaned_data['CustomerName']
				pw = cf.cleaned_data['CustomerPassword']
				pw_md5 = hashlib.md5(pw).hexdigest()
				customer.CustomerPassword = pw_md5
				customer.CustomerEmail = cf.cleaned_data['CustomerEmail']
				customer.CustomerAddress = cf.cleaned_data['CustomerAddress']
				customer.CustomerTelephone = cf.cleaned_data['CustomerTelephone']
				#write into db
				customer.save()
				request.session['UserType'] = cf.cleaned_data['identity']
				request.session['UserAccount'] = cf.cleaned_data['CustomerAccount']
				request.session['UserID'] = customer.id
				return HttpResponseRedirect('/')
				# return render_to_response('Homepage.html', locals(), context_instance=RequestContext(request))
			else: 
			#返回注册成功页面
				seller = Seller()
				seller.SellerAccount = cf.cleaned_data['CustomerAccount']
				cu=Seller.objects.filter(SellerAccount=seller.SellerAccount)
				if len(cu) == 1:
					duplicate=True
					return render_to_response('register.html',locals(), context_instance=RequestContext(request))
				seller.SellerName = cf.cleaned_data['CustomerName']
				pw = cf.cleaned_data['CustomerPassword']
				pw_md5 = hashlib.md5(pw).hexdigest()
				seller.SellerPassword = pw_md5
				seller.SellerEmail = cf.cleaned_data['CustomerEmail']
				seller.SellerAddress = cf.cleaned_data['CustomerAddress']
				seller.SellerTelephone = cf.cleaned_data['CustomerTelephone']
				#write into db
				seller.save()
				request.session['UserType'] = cf.cleaned_data['identity']
				request.session['UserAccount'] = cf.cleaned_data['CustomerAccount']
				request.session['UserID'] = seller.id
				return HttpResponseRedirect('/addshop')
				# return render_to_response('Homepage.html', locals(), context_instance=RequestContext(request))
	else:
		cf = CustomerForm()
		#cf = CustomerForm(request.POST)
	return render_to_response('register.html',{'cf':cf}, context_instance=RequestContext(request))

#/myinfo
def info(request):
	UserID = request.session['UserID']
	UserType = request.session['UserType']
	#UserName = request.session['UserName']
	if request.method == "POST":
		cf = CustomerForm2(request.POST)
		if cf.is_valid():
			#get form
			if UserType == 'C':
				customer = Customer.objects.get(id = UserID)
				customer.CustomerAccount = cf.cleaned_data['CustomerAccount']
				customer.CustomerName = cf.cleaned_data['CustomerName']
				pw = cf.cleaned_data['CustomerPassword']
				pw_md5 = hashlib.md5(pw).hexdigest()
				customer.CustomerPassword = pw_md5
				customer.CustomerEmail = cf.cleaned_data['CustomerEmail']
				customer.CustomerAddress = cf.cleaned_data['CustomerAddress']
				customer.CustomerTelephone = cf.cleaned_data['CustomerTelephone']
				#write into db
				customer.save()
				return render_to_response('success.html',{'UserType':'C','UserName':customer.CustomerName})
			else: 
				seller = Seller.objects.get(id = UserID)
				seller.SellerAccount = cf.cleaned_data['CustomerAccount']
				seller.SellerName = cf.cleaned_data['CustomerName']
				pw = cf.cleaned_data['CustomerPassword']
				pw_md5 = hashlib.md5(pw).hexdigest()
				seller.SellerPassword = pw_md5
				seller.SellerEmail = cf.cleaned_data['CustomerEmail']
				seller.SellerAddress = cf.cleaned_data['CustomerAddress']
				seller.SellerTelephone = cf.cleaned_data['CustomerTelephone']
				#write into db
				seller.save()
				return render_to_response('success.html',{'UserType':'S','UserName':seller.SellerName})
	else:
		if UserType == 'C':
			user = Customer.objects.get(id=UserID)
			UserAccount = user.CustomerAccount
			UserEmail = user.CustomerEmail
			UserAddress = user.CustomerAddress
			UserTel = user.CustomerTelephone
			UserName = user.CustomerName
		else:
			user = Seller.objects.get(id=UserID)
			UserAccount = user.SellerAccount
			UserEmail = user.SellerEmail
			UserAddress = user.SellerAddress
			UserTel = user.SellerTelephone
			UserName = user.SellerName
		data = {
			'identity':UserType,
			'CustomerAccount':UserAccount,
			'CustomerName':UserName,
			'CustomerEmail':UserEmail,
			'CustomerAddress':UserAddress,
			'CustomerTelephone':UserTel,
			}
		cf = CustomerForm2(data)
	return render_to_response('myinfo.html',locals(), context_instance=RequestContext(request))

def getCommodity(request, id):  #/commodity/id/ 返回ID=id 的Commodity
	
	commodity = Commodity.objects.get(id = int(id))
	return render_to_response('Customer_CommodityInfo.html', {'commodity': commodity})

def login(request):
	wrongpw = False  #wrongpw == True 代表密码错误
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			user = False
			UserAccount = uf.cleaned_data['UserAccount']
			pw = uf.cleaned_data['UserPassword']
			pw_md5 = hashlib.md5(pw).hexdigest()
			UserPassword = pw_md5
			if uf.cleaned_data['identity'] == 'C':
				try:
					user = Customer.objects.get(CustomerAccount__exact = UserAccount, CustomerPassword__exact = UserPassword)
					if user:
						request.session['UserType'] = uf.cleaned_data['identity']
						request.session['UserAccount'] = UserAccount
						request.session['UserID'] = user.id
						#return render_to_response('Homepage.html', locals(), context_instance=RequestContext(request))
						return HttpResponseRedirect('/index/')
					else:
						wrongpw = True
						return render_to_response('login.html', locals(), context_instance=RequestContext(request))
				except:
					pass
			else:
				try:
					user = Seller.objects.get(SellerAccount__exact = UserAccount, SellerPassword__exact = UserPassword)
					if user:
						request.session['UserType'] = uf.cleaned_data['identity']
						request.session['UserAccount'] = UserAccount
						request.session['UserID'] = user.id
						#return render_to_response('index.html',{'customer':user})
						return HttpResponseRedirect('/seller/home')#sellerHomepage 代表entershop
					else:
						wrongpw = True
						return render_to_response('login.html', locals(), context_instance=RequestContext(request))
				except:
					pass			
	else:
		uf = UserForm()
	return render_to_response('login.html', {'uf': uf, 'wrongpw': wrongpw}, context_instance=RequestContext(request))

def index(request):
	UserID = request.session.get('UserID', False)#, 'anybody')
	UserType = request.session.get('UserType')
	UserAccount = request.session.get('UserAccount')
	homeshopadv = HomeShopAdv.objects.filter(ApplyState=True)
	homecommodityadv = HomeCommodityAdv.objects.filter(ApplyState=True)
	bulletin = System.objects.get(id = 1)
	if UserID and UserType == 'C':
		user = Customer.objects.get(id = UserID)
		UserName = user.CustomerName
		#locals() -> {'UserName': UserName, 'UserType': UserType, 'UserID':UserID}
		#return HttpResponse(user.CustomerAccount)
		return render_to_response('Homepage.html', locals(), context_instance=RequestContext(request))
	elif UserID and UserType == 'S':
		user = Seller.objects.get(id = UserID)
		UserName = user.SellerName
		#locals() -> {'UserName': UserName, 'UserType': UserType, 'UserID':UserID}
		return render_to_response('Homepage.html', locals(), context_instance=RequestContext(request))
	else:
		return render_to_response('Homepage.html', locals(), context_instance=RequestContext(request))


def logout(request):
	session = request.session.get('UserID', False)
	if session:
		del request.session['UserID']
		del request.session['UserType']
		del request.session['UserAccount']
		# return render_to_response('logout.html', {'CustomerName': session}, context_instance=RequestContext(request))
		return HttpResponseRedirect('/index/')##########
	else:
		return HttpResponse('You have not login!')

#查看销售历史
def salesHistory(request, time):
	if request.session.get('UserID', False):
		UserID = request.session['UserID']
		UserType = request.session['UserType']
		UserAccount = request.session['UserAccount']
		UserName = UserAccount
	else:
		UserID = None
		UserType = None
		UserAccount = None
	shopID = Shop.objects.get(SellerID = UserID)
	shopOrder = ShopOrder.objects.filter(ShopID = shopID)
	SalesHistoryList = []
	now = datetime.datetime.now()
	for so in shopOrder:
		SaleList = OrderList.objects.filter(ShopOrderID = so, OrderListState__gte = 7)
		for sl in SaleList:
			if time == "all":
				SalesHistoryList.append(sl)
			elif time == "year":
				if sl.OrderListDate.year == now.year:
					SalesHistoryList.append(sl)
			elif time == "month":
				if sl.OrderListDate.month == now.month and sl.OrderListDate.year == now.year:
					SalesHistoryList.append(sl)
			elif time == "day":
				if sl.OrderListDate.day == now.day and sl.OrderListDate.month == now.month and sl.OrderListDate.year == now.year:
					SalesHistoryList.append(sl)
	totalvalue = 0
	for shl in SalesHistoryList:
		totalvalue = totalvalue + shl.CommodityID.SellPrice * shl.OrderAmount

	SalesHistoryList1 = []
	for so in shopOrder:
		SaleList = OrderList.objects.filter(ShopOrderID = so, OrderListState__in = [1,2,3,4,5,6])
		for sl in SaleList:
			SalesHistoryList1.append(sl)
	totalvalue1 = 0
	for shl1 in SalesHistoryList1:
		totalvalue1 = totalvalue1 + shl1.CommodityID.SellPrice * shl1.OrderAmount


	seller = Seller.objects.get(id=UserID)
	try:
		shop = Shop.objects.get(SellerID = seller)
		commoditylist = Commodity.objects.filter(ShopID = shop)
		shopadvlist = Shop.objects.filter(SellerID = seller, IsAdv = True)
		commodityadvlist = Commodity.objects.filter(ShopID = shop, IsAdv = True)
	except:
		shop = None
	return render_to_response('SellerSaleHistory.html', locals())


#店铺管理订单（查看订单并确认）
def checkOrder(request):
	if request.session.get('UserID', False):
		UserID = request.session['UserID']
		UserType = request.session['UserType']
		UserAccount = request.session['UserAccount']
		UserName = UserAccount
	else:
		UserID = None
		UserType = None
		UserAccount = None
	shopID = Shop.objects.get(SellerID = UserID)
	shopOrder = ShopOrder.objects.filter(ShopID = shopID, ShopOrderState = 0)
	orderList = []
	for so in shopOrder:
		List = OrderList.objects.filter(ShopOrderID = so, OrderListState = 0)
		for ol in List:
			orderList.append(ol)
	seller = Seller.objects.get(id=UserID)
	try:
		shop = Shop.objects.get(SellerID = seller)
		commoditylist = Commodity.objects.filter(ShopID = shop)
		shopadvlist = Shop.objects.filter(SellerID = seller, IsAdv = True)
		commodityadvlist = Commodity.objects.filter(ShopID = shop, IsAdv = True)
	except:
		shop = None
	#return HttpResponse(orderList[0])
	return render_to_response('checkOrder.html', locals())


def removeOrderList(request):
	if request.session.get('UserID', False):
		UserID = request.session['UserID']
		UserType = request.session['UserType']
		UserAccount = request.session['UserAccount']
		UserName = UserAccount
	else:
		UserID = None
		UserType = None
		UserAccount = None
	if 'id' in request.GET:
		content = request.GET['content']
		ol = OrderList.objects.get(id = request.GET['id'])
		ol.OrderListState = 1
		ol.ShipNo = content
		ol.save()
		so = ShopOrder.objects.get(id = ol.ShopOrderID.id)
		so.ShopOrderState = 1
		so.save()
		co = CustomerOrder.objects.get(id = ol.CustomerOrderID.id)
		co.CustomerOrderState = 1
		co.save()
		income = 0
		income = income + ol.CommodityID.SellPrice * ol.OrderAmount
		incomeAmount = income * System.objects.get(id = 1).ComissionRate
		tmp = Income.objects.get(id = 1)
		tmp.IncomeAmount = tmp.IncomeAmount + incomeAmount
		tmp.save()
	else:
		ol = None
	return HttpResponse("You modified: "+ ol.CommodityID.CommodityName+"from Orderlist")


def refund(request):
	if request.session.get('UserID', False):
		UserID = request.session['UserID']
		UserType = request.session['UserType']
		UserAccount = request.session['UserAccount']
		UserName = UserAccount
	else:
		UserID = None
		UserType = None
		UserAccount = None
	shopID = Shop.objects.get(SellerID = UserID)
	shopOrder = ShopOrder.objects.filter(ShopID = shopID, ShopOrderState = 4)
	orderList = []
	for so in shopOrder:
		List = OrderList.objects.filter(ShopOrderID = so, OrderListState = 4)
		for ol in List:
			orderList.append(ol)
	seller = Seller.objects.get(id=UserID)
	try:
		shop = Shop.objects.get(SellerID = seller)
		commoditylist = Commodity.objects.filter(ShopID = shop)
		shopadvlist = Shop.objects.filter(SellerID = seller, IsAdv = True)
		commodityadvlist = Commodity.objects.filter(ShopID = shop, IsAdv = True)
	except:
		shop = None
	#return HttpResponse(orderList[0])
	return render_to_response('Seller_ReturnAndRefund.html', locals())



def modifyOrderList1(request):
	if request.session.get('UserID', False):
		UserID = request.session['UserID']
		UserType = request.session['UserType']
		UserAccount = request.session['UserAccount']
		UserName = UserAccount
	else:
		UserID = None
		UserType = None
		UserAccount = None
	if 'id' in request.GET:
		ol = OrderList.objects.get(id = request.GET['id'])
		ol.OrderListState = 5
		ol.save()
		so = ShopOrder.objects.get(id = ol.ShopOrderID.id)
		so.ShopOrderState = 5
		so.save()
		co = CustomerOrder.objects.get(id = ol.CustomerOrderID.id)
		co.CustomerOrderState = 5
		co.save()
	else:
		ol = None
	return HttpResponse("You modified: "+ ol.CommodityID.CommodityName+"from Orderlist")

def modifyOrderList2(request):
	if request.session.get('UserID', False):
		UserID = request.session['UserID']
		UserType = request.session['UserType']
		UserAccount = request.session['UserAccount']
		UserName = UserAccount
	else:
		UserID = None
		UserType = None
		UserAccount = None
	if 'id' in request.GET:
		ol = OrderList.objects.get(id = request.GET['id'])
		ol.OrderListState = 7
		ol.save()
		so = ShopOrder.objects.get(id = ol.ShopOrderID.id)
		so.ShopOrderState = 7
		so.save()
		co = CustomerOrder.objects.get(id = ol.CustomerOrderID.id)
		co.CustomerOrderState = 7
		co.save()
	else:
		ol = None
	return HttpResponse("You modified: "+ ol.CommodityID.CommodityName+"from Orderlist")


def adminIncome(request, time):
	#comission money
	orderList = []
	orders = OrderList.objects.filter(OrderListState__in = [7,8])
	now = datetime.datetime.now()
	for ol in orders:
		if time == "all":
			orderList.append(ol)
		elif time == "year":
			if ol.OrderListDate.year == now.year:
				orderList.append(ol)
		elif time == "month":
			if ol.OrderListDate.month == now.month and ol.OrderListDate.year == now.year:
				orderList.append(ol)
		elif time == "day":
			if ol.OrderListDate.day == now.day and ol.OrderListDate.month == now.month and ol.OrderListDate.year == now.year:
				orderList.append(ol)
	conserveorderList = []
	conserveorders = OrderList.objects.filter(OrderListState__in = [0,1,2,3,4,5,6])
	for ol in conserveorders:
		conserveorderList.append(ol)
	totalvalue = 0
	for shl in orderList:
		totalvalue = totalvalue + shl.CommodityID.SellPrice * shl.OrderAmount
	totalcomission = totalvalue * 0.02
	#adv income from shopAdv
	shopAdvNum = 0
	shopAdv = []
	shop = Shop.objects.all()
	for s in shop:
		if s.IsAdv == True:
			shopAdv.append(s)
			shopAdvNum = shopAdvNum + 1
	shopAdvIncome = shopAdvNum * 2000.0
	##adv income from commodityAdv
	commodityAdvNum = 0
	commodityAdv = []
	commodity = Commodity.objects.all()
	for c in commodity:
		if c.IsAdv == True:
			commodityAdv.append(c)
			commodityAdvNum = commodityAdvNum + 1
	commodityAdvIncome = commodityAdvNum * 2000.0
	totalIncome = shopAdvIncome + commodityAdvIncome
	return render_to_response('adminIncome.html', locals())
