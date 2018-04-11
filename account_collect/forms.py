# -*- coding: utf-8 -*-
from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(label=u'导入账号', initial=u'导入文件名')
    file = forms.FileField()
