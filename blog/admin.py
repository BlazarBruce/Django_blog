"""
功能：后台管理系统的创建
用户：Bruce
密码：123456
创建超级用户：python manage.py createsuperuser

注意：该py文件只是完成了怎么用（配置）、需要对源码流程进行梳理！！！！

"""
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

from .models import Category, Tag, Post
from .adminforms import PostAdminForm
from Django_cbv.custom_site import custom_site
from Django_cbv.base_admin import BaseOwnerAdmin


class PostInline(admin.TabularInline):  # StackedInline 工口e 样式不同

    fields = ("title", "desc"),
    extra = 1  # 控制额外多几个
    model = Post


# 在admin中注册类、添加用户自己的信息
@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):  # 分类后台管理类、需要了解源码流程
    inlines = [PostInline, ]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        """展示分类下有多少篇文章"""
        return obj.post_set.count()

    post_count.short_description = '文章数量'

    def __str__(self):
        return self.name


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):  # 标签后台管理类、需要了解源码流程
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


# 通过继承Django admin 提供的SimpleListFilter 类来实现自定义过滤器，
class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户的分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        """返回要展示的内容和l查询用的id (就是上面Query 用的）"""
        return Category.objects.filter(owner=request.user).value_list('id', 'name')

    def queryset(self, request, queryset):
        """根据URL Query 的内容返回列表页数据"""
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):  # 文章后台管理类、需要了解远吗流程
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status',
        'created_time', 'owner', 'operator'
    ]  # 用来配置列表页面展示哪些字段
    list_display_links = []  # 用来配置哪些字段可以作为链接，点击它们，可以进入编辑页面。

    list_filter = ['category', ]  # 配置页面过滤器，需要通过哪些字段来过滤列表页。
    # list_filter = ['CategoryOwnerFilter', ]  # 配置页面过滤器，需要通过哪些字段来过滤列表页。
    search_fields = ['title', 'category__name']  # 配置搜索字段

    actions_on_top = True  # 动作相关的配置，是否展示在顶部
    actions_on_bottom = True  # 动作相关的配置，是否展示在底部

    # 编辑页面
    save_on_top = True  # 保存、编辑、编辑并新建按钮是否在顶部展示

    exclude = ['owner']

    """
    fields = (
        ("category", "title"),
        'desc',
        'status',
        'content',
        'tag',
    )
    """

    fieldsets = (
        ('基础信息',{
        'description': '基础配置描述',
        'fields': (("title", "category"),
        'status',
         ),
         }),

        ('内容',  {
            'fields':(
                "desc",
                "content"
            ),
        }),

        ('额外信息', {
            'classes':('collapse',),
            'fields': ("tag",),
        }

    ))

    # filter_horizontal = ('tag',)
    filter_vertical = ('tag',)  # 报错 ！！！！

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('custom_site:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    class Media:
        """我们可以通过自定义Media 类来往页面上增加想要添加的JavaScript 以及css资源"""
        css = {'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",)}
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


# 查看日志功能
@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):  # 日志后台管理类、需要、了解源码流程
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
