#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from system.models import *

# Create your views here.

def Seller_ShopBaseInfo(request):
	