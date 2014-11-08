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
import sys
import os
import os.path
import shutil

def manageadv(request):
    render_to_response('')

def db(request): #show the db page
    cur_path = sys.path[0] # anybuy/
    listdir = os.listdir(cur_path)
    backup_db_dir = os.path.join(cur_path, 'db_backup')
    cur_db_dir = cur_path
    cur_db = os.path.join(cur_db_dir, "db.sqlite3")
    cur_date = time.strftime('%Y%m%d',time.localtime(time.time()))
    backup_db = os.path.join(cur_db_dir, "db.sqlite3", cur_date)
    # shutil.move(cur_db_dir,backup_db_dir+"db.sqlite3")
    backup_list=os.listdir(os.path.join(cur_db_dir, "db_backup"))
    return render_to_response('managedb.html', locals())

# shutil.copy("/Users/eric/Documents/Programming/parknshop/Pro/anybuy/db.sqlite3","/Users/eric/Documents/Programming/parknshop/Pro/anybuy/db.sqlite333")
def backupdb(request):
    # backup_db_dir = os.path.join(cur_path, 'db_backup')
    cur_db_dir = sys.path[0] # anybuy/
    cur_db = os.path.join(cur_db_dir, "db.sqlite3")
    cur_date = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    backup_db = os.path.join(cur_db_dir, "db_backup", "db-manu-"+cur_date)
    shutil.copyfile(cur_db, backup_db)
    db_backupls = os.listdir(os.path.join(cur_db_dir, "db_backup"))
    return HttpResponse(db_backupls[-1])


def restoredb(request):
    re_db = request.GET['db']
    cur_db_dir = sys.path[0] # anybuy/
    cur_db = os.path.join(cur_db_dir, "db.sqlite3")
    backup_db = os.path.join(cur_db_dir, "db_backup", re_db)
    shutil.copyfile(backup_db, cur_db)
    return HttpResponse(os.listdir(os.path.join(cur_db_dir, "db_backup")))


def deletedb(request):
    rm_db = request.GET['db']
    cur_db_dir = sys.path[0] # anybuy/
    backup_db = os.path.join(cur_db_dir, "db_backup", rm_db)
    os.remove(backup_db)
    return HttpResponse(rm_db)