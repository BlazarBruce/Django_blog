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
from django.urls import path
from .custom_site import custom_site

from blog.views import post_list, post_detail
from config.views import Links

urlpatterns = [
    # 路由配置及参数传递均没有问题
    url(r'^$', post_list),
    url(r'^category/(?P<category_id>\d+)/$', post_list),
    url(r'^tag/(?P<tag_id>\d+)/$', post_list),
    url(r'^post/(?P<post_id>\d+).html$', post_detail),
    url(r'^links/$', Links),

    # path('admin/', admin.site.urls),  # 对应一个site
    url(r'^super_admin/', admin.site.urls),  # 对应一个site (urt与path相比、url支持正则）用来管理用户
    url(r'^admin/', custom_site.urls),  # 对应一个site (urt与path相比、url支持正则）用来管理业务

]

