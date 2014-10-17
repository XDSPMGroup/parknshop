# Create your views here.
#coding=utf-8
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from account.models import *

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    passworld = forms.CharField(label='密码：',widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件：')

	CustomerAccount = forms.CharField(label='Username:', max_length=64)
	CustomerName = forms.CharField(label='Name:', max_length=64)
	CustomerPassword = forms.CharField(label='password:', widget=forms.PasswordInput(), max_length=16)
	#CustomerType = forms.CharField(label='Type：', max_length=1, choices=CustomerTypeChoices,blank=True)
	CustomerTelephone = forms.CharField(label='Tel:',max_length=64,blank=True)
	CustomerEmail = forms.EmailField()
	CustomerAddress = forms.TextField(label='e-mail:',blank=True)
# Create your views here.
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            passworld = uf.cleaned_data['passworld']
            email = uf.cleaned_data['email']
            #将表单写入数据库
            user = Customer()
            user.username = username
            user.passworld = passworld
            user.email = email
            user.save()
            #返回注册成功页面
            return render_to_response('success.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})