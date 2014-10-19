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
class CustomerForm(forms.Form):
	CustomerAccount = forms.CharField(label='Account:', max_length=64)
	CustomerName = forms.CharField(label='Name:', max_length=64)
	CustomerPassword = forms.CharField(label='Password:', widget=forms.PasswordInput(), max_length=16)
	#CustomerType = forms.CharField(label='Type：', max_length=1, choices=CustomerTypeChoices,blank=True)
	CustomerTelephone = forms.CharField(label='Tel:',max_length=64)
	CustomerEmail = forms.EmailField(label='E-mail:')
	CustomerAddress = forms.CharField(label='Address:')

class UserForm(forms.Form):
	identity = forms.ChoiceField(label='your identity:')
	UserAccount = forms.CharField(label='Account:', max_length=64)
	UserPassword = forms.CharField(label='Password:', widget=forms.PasswordInput(), max_length=16)

# Create your views here.

def register(request):
	if request.method == "POST":
		cf = CustomerForm(request.POST)
		if cf.is_valid():
			#get form
			customer = Customer()
			customer.CustomerAccount = cf.cleaned_data['CustomerAccount']
			customer.CustomerName = cf.cleaned_data['CustomerName']
			pw = cf.cleaned_data['CustomerPassword']
			pw_md5 = hashlib.md5(pw).hexdigest()
			customer.CustomerPassword = pw_md5[0:16]
			customer.CustomerEmail = cf.cleaned_data['CustomerEmail']
			customer.CustomerAddress = cf.cleaned_data['CustomerAddress']
			customer.CustomerTelephone = cf.cleaned_data['CustomerTelephone']
			#write into db
			customer.save()
			#返回注册成功页面
			return render_to_response('success.html',{'customer':customer})
	else:
		cf = CustomerForm()
		#cf = CustomerForm(request.POST)
	return render_to_response('register.html',{'cf':cf}, context_instance=RequestContext(request))

def search(request, keyword):  #/search/keyword/ 以keyword为关键字进行搜索，返回一个commodityList
	commodityList = Commodity.objects.filter(CommodityName__contains = keyword)
	return render_to_response('Customer_CommidityList.html', {'commodityList': commodityList, 'keyword': keyword})

def getCommodity(request, id):  #/commodity/id/ 返回ID=id 的Commodity
	commodity = Commodity.objects.get(CommodityName = int(id))
	return render_to_response('Customer_CommodityInfo.html', {'commodity': commodity})

def login(request):
	wrongpw = False  #wrongpw == True 代表密码错误
	if request.method == 'POST':
		uf = UserForm(request.POST)
		if uf.is_valid():
			UserAccount = uf.cleaned_data['UserAccount']
			pw = uf.cleaned_data['UserPassword']
			pw_md5 = hashlib.md5(pw).hexdigest()
			UserPassword = pw_md5[0:16]
			user = Customer.objects.filter(CustomerAccount__exact = UserAccount, CustomerPassword__exact = UserPassword)
			if user:
				request.session['UserAccount'] = UserAccount
				#return render_to_response('index.html',{'customer':user})
				return HttpResponseRedirect('/account/index/')
			else:
				wrongpw = True
				return render_to_response('login.html', {'uf': uf, 'wrongpw': wrongpw}, context_instance=RequestContext(request))
	else:
		uf = UserForm()
		return render_to_response('login.html', {'uf': uf, 'wrongpw': wrongpw}, context_instance=RequestContext(request))

def index(request):
	UserName = request.session.get('UserAccount', False)#, 'anybody')
	if UserName:
		return render_to_response('index.html', {'username': UserName}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/account/login/')

def logout(request):
	session = request.session.get('UserAccount', False)
	if session:
		del request.session['UserAccount']
		return render_to_response('logout.html', {'CustomerName': session}, context_instance=RequestContext(request))
	else:
		return HttpResponse('You have not login!')



