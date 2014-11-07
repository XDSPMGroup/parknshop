#coding=utf-8

from django.shortcuts import render
from django import forms
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from system.models import *
import time
import datetime
from PIL import Image
import hashlib

def manageadv(request):
    render_to_response('')