# -*- coding: utf-8 -*-
"""
@name: 后台用到的form
@function：Form 跟Model其实是相合在一起的，或者说Form 跟Model 的逻辑是一致的， Model是对数据库中
字段的抽象，Form 是对用户输入以及Model 中要展示数据的抽象。
@step:
@author: Bruce
@contact: zhu.chaoqiang@byd.com
@Created on: 2019/10/18 10:10
"""
from django import forms

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)


