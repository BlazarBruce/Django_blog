# -*- coding: utf-8 -*-
"""
@name:        
@function：   
@step:        
@author: Bruce
@contact: zhu.chaoqiang@byd.com
@Created on: 2019/10/22 10:24

"""
# 问题一：如何查看三方文档的功能？
# 1、官方文档
# 2、查看源码、可以到对应的虚拟环境、库安装的目录下进行源码查看、也可以在解释器部分查看

# 问题二：Django提供了哪些组件？


# 问题三：为什么要重载（重写）父类方法
#        ——父类的方法不适合子类的场景、子类需要对其进行个性化的改造


# 问题四：处理数据与样式的分开
# 后端：主要工作室处理数据
# 前端：主要工作室处理样式
# 当一个人开发的时候，要把处理数据过程与展示过程分开、并且先处理数据过程

# 问题五：在模板HTML中也可以配置跳转路由、并且可以实现GET方法拼接字符串传参、POST方法form表单传参

# 问题六：可以通过模板反向url解析、和reverse()反向解析实现解耦

# 源码手动安装Python库
# 比如：手动安装requests
#
# 先下载requests包 https://github.com/kennethreitz/requests
# 解压下载的zip包
# 进入有setup.py 的目录 ，用windows的cmd
# 先执行 python setup.py build
# 然后执行 python setup.py install
# 如果不出什么问题，提示安装成功
# 新建立一个测试项目，import requests 
