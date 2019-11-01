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
    分组命名正则表达式组的语法:(?P<name>pattern)，其中name是组的名称，pattern是要匹配的模式。
"""
from django.contrib import admin
from django.conf.urls import url, include
from .custom_site import custom_site
from django.contrib.sitemaps import views as sitemap_views
from django.views.decorators.cache import cache_page
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap

from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
from config.views import LinkListView
from comment.views import CommentView
from blog.apis import post_list, PostList
from blog.api import PostViewSet, CategoryViewSet
from rest_framework.documentation import include_docs_urls  # 用于配置接口文档
from rest_framework.routers import DefaultRouter  # Django rest framework 的路由配置


router = DefaultRouter()
router.register(r'post', PostViewSet, base_name='api-post')
router.register(r'category', CategoryViewSet, base_name='api-category')



urlpatterns = [
    # 路由配置及参数传递均没有问题
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^search/$', SearchView.as_view(), name='search'),  # 用于搜索功能
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    # 分组命名匹配、这个url有问题！！！对于FBV没有问题
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', cache_page(60 * 20, key_prefix='sitemap_cache_')(sitemap_views.sitemap),{'sitemaps': {'posts': PostSitemap}}),
    url(r'^apis/post', post_list, name='post-list'),  # 该url目前无法访问
    url(r'^api/docs/', include_docs_urls(title='typeidea apis')),  # 配置接口文档
    url(r'^api/', include(router.urls, namespace='api')),  # 配置接口文档

    # 后台管理url
    url(r'^super_admin/', admin.site.urls, name='super-admin'),  # 超级用户
    url(r'^admin/', custom_site.urls, name='admin'),  # 普通用户

]
