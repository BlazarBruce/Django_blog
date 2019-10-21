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
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from .custom_site import custom_site

urlpatterns = [
    # path('admin/', admin.site.urls),  # 对应一个site
    url(r'^super_admin/', admin.site.urls),  # 对应一个site (urt与path相比、url支持正则）用来管理用户
    url(r'^admin/', custom_site.urls)  # 对应一个site (urt与path相比、url支持正则）用来管理业务

]

