"""Django_cbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    分组命名正则表达式组的语法是(?P<name>pattern)，其中name是组的名称，pattern是要匹配的模式。
"""
from django.contrib import admin
from django.conf.urls import url
from .custom_site import custom_site

from blog.views import post_list, post_detail, IndexView, CategoryView, TagView, PostDetailView
from config.views import Links

urlpatterns = [
    # 路由配置及参数传递均没有问题
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-id'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-id'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^links/$', Links, name='links'),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),  # 对应一个site (urt与path相比、url支持正则）用来管理用户
    url(r'^admin/', custom_site.urls, name='admin'),  # 对应一个site (urt与path相比、url支持正则）用来管理业务

]

