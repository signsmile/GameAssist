# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from datetime import datetime
from time import time
from .models import GameName, OPSystem, Platform, Sex, Pet, Goods, Character, Account, NewAccount, Config

@admin.register(GameName, OPSystem, Platform, Sex, Pet, Goods, Character)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    list_display = ('id', 'create_date_fmt', 'username', 'pwd', 'platform', 'gamename', 'opsystem', 'precinct',
                    'sex', 'pet', 'goods', 'character', 'remark')
    list_filter = ('platform', 'gamename', 'opsystem', 'precinct', 'sex', 'pet', 'goods', 'character')
    # ordering = ('id',)
    # date_hierarchy = 'create_date'

    def create_date_fmt(self, obj):
        return obj.create_date.strftime("%Y-%m-%d %H:%M:%S")
    create_date_fmt.short_description = u'日期'

@admin.register(NewAccount)
class NewAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'create_date_fmt', 'username', 'pwd', 'platform', 'gamename' , 'used' )
    ordering = ('-create_date',)
    def create_date_fmt(self, obj):
        return obj.create_date.strftime("%Y-%m-%d %H:%M:%S")
    create_date_fmt.short_description = u'日期'

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')