# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse

from .models import GameName, OPSystem, Platform, Sex, Pet, Goods, Character, Account

def index(request):
    return HttpResponseRedirect('/admin/account_collect/account/')

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
