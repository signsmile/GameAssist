# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models

class GameName(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def update_game_names():
        names = [u'口袋妖怪复刻', u'口袋妖怪起源',  u'神无月', u'火影忍者']
        GameName.objects.all().delete()
        for i, name in enumerate(names):
            GameName(id=i+1, name=name).save()

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u'游戏'
        verbose_name_plural = u'游戏'

class OPSystem(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def update_opsystem():
        names = [u'IOS', u'Android']
        OPSystem.objects.all().delete()
        for i, name in enumerate(names):
            OPSystem(id=i+1, name=name).save()

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u'系统'
        verbose_name_plural = u'系统'

class Platform(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def update_platform():
        names = [u'果盘', u'优趣', u'虫虫', u'TT', u'爱应用', u'乐8', u'快用', u'当乐']
        Platform.objects.all().delete()
        for i, name in enumerate(names):
            Platform(id=i+1, name=name).save()

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u'平台'
        verbose_name_plural = u'平台'

class Sex(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def update_sex():
        names = [u'男', u'女']
        Sex.objects.all().delete()
        for i, name in enumerate(names):
            Sex(id=i+1, name=name).save()

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u'性别'
        verbose_name_plural = u'性别'

class Pet(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def update_pets():
        names = [u'妙蛙种子', u'小火龙', u'杰尼龟']
        Pet.objects.all().delete()
        for i, name in enumerate(names):
            Pet(id=i+1, name=name).save()

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u'宠物'
        verbose_name_plural = u'宠物'

class Goods(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def update_goods():
        names = [u'狃拉', u'剧毒珠', u'伊布', u'急冻拳', u'打草结', u'吸收拳', u'冥想', u'振奋精神的绑带',
            u'剩饭', u'先攻之爪', u'巨大根茎', u'黑色淤泥', u'铁面忍者', u'高级狩猎券']
        Goods.objects.all().delete()
        for i, name in enumerate(names):
            Goods(id=i+1, name=name).save()

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u'物品'
        verbose_name_plural = u'物品'

class Character(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def update_characters():
        names = [u'胆小', u'天真', u'开朗', u'大胆', u'保守', u'沉着', u'固执', u'急躁', u'慎重', u'淘气']
        Character.objects.all().delete()
        for i, name in enumerate(names):
            Character(id=i+1, name=name).save()

    def __str__(self):
        return self.name.encode('utf-8')

    class Meta:
        verbose_name = u'性格'
        verbose_name_plural = u'性格'

class Account(models.Model):
    username = models.CharField(max_length=50, verbose_name=u'用戶名')
    pwd = models.CharField(max_length=100, verbose_name=u'密码')
    precinct = models.CharField(max_length=100, verbose_name=u'选区')
    remark = models.CharField(max_length=255, verbose_name=u'备注')
    create_date = models.DateTimeField(default=timezone.now)

    gamename = models.ForeignKey(GameName, default=None, on_delete=models.CASCADE, verbose_name=u'游戏')
    opsystem = models.ForeignKey(OPSystem, default=None, on_delete=models.CASCADE, verbose_name=u'系统')
    platform = models.ForeignKey(Platform, default=None, on_delete=models.CASCADE, verbose_name=u'平台')
    sex = models.ForeignKey(Sex, default=None, on_delete=models.CASCADE, verbose_name=u'性别')
    pet = models.ForeignKey(Pet, default=None, on_delete=models.CASCADE, verbose_name=u'宠物')
    goods = models.ForeignKey(Goods, default=None, on_delete=models.CASCADE, verbose_name=u'物品')
    character = models.ForeignKey(Character, default=None, on_delete=models.CASCADE, verbose_name=u'性格')

    class Meta:
        verbose_name = u'账号记录'
        verbose_name_plural = u'账号记录'

def update_db():
    GameName.update_game_names()
    OPSystem.update_opsystem()
    Platform.update_platform()
    Sex.update_sex()
    Pet.update_pets()
    Goods.update_goods()
    Character.update_characters()
