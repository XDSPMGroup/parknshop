# Create your views here.
#coding=utf-8
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from system.models import *
import hashlib

#定义表单模型
IDENTITY = (
('C', 'Customer'),
('S', 'Seller'),
)

class CustomerForm(forms.Form):
	identity = forms.ChoiceField(label='your identity:', choices=IDENTITY)
	CustomerAccount = forms.CharField(label='Account:', max_length=64)
	CustomerName = forms.CharField(label='Name:', max_length=64)
	CustomerPassword = forms.CharField(label='Password:', widget=forms.PasswordInput(), max_length=16)
	#CustomerType = forms.CharField(label='Type：', max_length=1, choices=CustomerTypeChoices,blank=True)
	CustomerTelephone = forms.CharField(label='Tel:',max_length=64)
	CustomerEmail = forms.EmailField(label='E-mail:')
	CustomerAddress = forms.CharField(label='Address:')

class CustomerForm2(forms.Form):
	#identity = forms.ChoiceField(label='your identity:', choices=IDENTITY)
	CustomerAccount = forms.CharField(label='Account:', max_length=64)
	CustomerName = forms.CharField(label='Name:', max_length=64)
	CustomerPassword = forms.CharField(label='Password:', widget=forms.PasswordInput(), max_length=16)
	#CustomerType = forms.CharField(label='Type：', max_length=1, choices=CustomerTypeChoices,blank=True)
	CustomerTelephone = forms.CharField(label='Tel:',max_length=64)
	CustomerEmail = forms.EmailField(label='E-mail:')
	CustomerAddress = forms.CharField(label='Address:')

class UserForm(forms.Form):
	identity = forms.ChoiceField(label='your identity:', choices=IDENTITY)
	UserAccount = forms.CharField(label='Account:', max_length=64)
	UserPassword = forms.CharField(label='Password:', widget=forms.PasswordInput(), max_length=16)

# Create your views here.

def register(request):
	if request.method == "POST":
		cf = CustomerForm(request.POST)
		if cf.is_valid():
			#get form
			if cf.cleaned_data['identity'] == 'C':
				customer = Customer()
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
			#返回注册成功页面
				seller = Seller()
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
						#return render_to_response('index.html',{'customer':user})
						return HttpResponseRedirect('/index/')
					else:
						wrongpw = True
						return render_to_response('login.html', {'uf': uf, 'wrongpw': wrongpw}, context_instance=RequestContext(request))
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
						return HttpResponseRedirect('/sellerHomepage/')#sellerHomepage 代表entershop
					else:
						wrongpw = True
						return render_to_response('login.html', {'uf': uf, 'wrongpw': wrongpw}, context_instance=RequestContext(request))
				except:
					pass			
	else:
		uf = UserForm()
	return render_to_response('login.html', {'uf': uf, 'wrongpw': wrongpw}, context_instance=RequestContext(request))

def index(request):
	UserID = request.session.get('UserID', False)#, 'anybody')
	UserType = request.session.get('UserType')
	if UserID:
		user = Customer.objects.get(id = UserID)
		UserName = user.CustomerName
		#locals() -> {'UserName': UserName, 'UserType': UserType, 'UserID':UserID}
		return render_to_response('index.html', locals(), context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

def sellerHomepage(request):
	UserID = request.session.get('UserID', False)#, 'anybody')
	UserType = request.session.get('UserType')
	if UserID:
		user = Seller.objects.get(id = UserID)
		UserName = user.SellerName
		#locals() -> {'UserName': UserName, 'UserType': UserType, 'UserID':UserID}
		return render_to_response('sellerHomepage.html', locals(), context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')


def logout(request):
	session = request.session.get('UserID', False)
	if session:
		del request.session['UserID']
		return render_to_response('logout.html', {'CustomerName': session}, context_instance=RequestContext(request))
	else:
		return HttpResponse('You have not login!')

#def salesHistory(request):
	

