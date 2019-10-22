# -*- coding: utf-8 -*-
"""
@name:        
@function：自定义用户后台
@step:        
@author: Bruce
@contact: zhu.chaoqiang@byd.com
@Created on: 2019/10/18 10:45

"""
from django.contrib.admin import AdminSite

class CustomSite(AdminSite) :
    site_header ='东方不败'
    sitetitle ='东方不败管理后台'
    index_title = '首页'

custom_site = CustomSite(name="cus_admin")

