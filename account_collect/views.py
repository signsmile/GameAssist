# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import serializers

from .models import GameName, OPSystem, Platform, Sex, Pet, Goods, Character, Account, NewAccount, Config
from .forms import UploadFileForm

import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def index(request):
    return HttpResponseRedirect('/admin/account_collect/account/')

def test(request):
    return render(request, 'account_collect/index.html')

def addact(request):
    params = request.GET
    account = Account()
    if 'gamename_id' in params:
        account.gamename = GameName.objects.get(id=params['gamename_id'])
    if 'system_id' in params:
        account.opsystem = OPSystem.objects.get(id=params['system_id'])
    if 'platform_id' in params:
        account.platform = Platform.objects.get(id=params['platform_id'])
    if 'sex_id' in params:
        account.sex = Sex.objects.get(id=params['sex_id'])
    if 'pet_id' in params:
        account.pet = Pet.objects.get(id=params['pet_id'])
    if 'goods_id' in params:
        account.goods = Goods.objects.get(id=params['goods_id'])
    if 'character_id' in params:
        account.character = Character.objects.get(id=params['character_id'])
    if 'precinct' in params:
        account.precinct = params['precinct']
    if 'actnum' in params:
        account.username = params['actnum']
    if 'pwd' in params:
        account.pwd = params['pwd']
    if 'remark' in params:
        account.remark = params['remark']
    account.save()
    return HttpResponse("succeed")

def upload_account(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/admin/account_collect/newaccount/')
    else:
        form = UploadFileForm()
    return render(request, 'account_collect/upload_account.html', {'form': form})

def handle_uploaded_file(f):
    for line in f:
        account = line.split(u'-')
        if len(account) == 4 and not check_contain_chinese(account[0]) and account[0].isalnum():
            newAccount = NewAccount()
            newAccount.username, newAccount.pwd, newAccount.platform, newAccount.gamename = account
            newAccount.save()

def add_new_account(request):
    params = request.GET
    newAccount = NewAccount()
    if 'pwd' in params:
        newAccount.pwd = params['pwd']
    if 'actnum' in params:
        newAccount.username = params['actnum']
    if 'platform' in params:
        newAccount.platform = params['platform']
    if 'gamename' in params:
        newAccount.gamename = params['gamename']
    newAccount.save()
    return HttpResponse("succeed")

def get_new_account(request):
    config = Config.objects.filter(key="new_act_limit").first()
    if config is not None and \
        config.value.isdigit and \
        int(config.value) <= len(NewAccount.objects.filter(create_date__gte=datetime.date.today()).filter(used=True)):
        return HttpResponse("{'result':'Limit to %d'}" % int(config.value))

    newAccount = NewAccount.objects.filter(create_date__gte=datetime.date.today()).filter(used=False).first()
    if newAccount is None:
        return HttpResponse("{'result':'None'}")

    newAccount.used = True
    newAccount.save()

    result = "{'result':'success', 'actnum': %s, 'pwd': %s, 'platform': %s, 'gamename': %s}" % \
             (newAccount.username, newAccount.pwd, newAccount.platform, newAccount.gamename)
    return  HttpResponse(result)
    # return HttpResponse(serializers.serialize('json', [newAccount.]))
