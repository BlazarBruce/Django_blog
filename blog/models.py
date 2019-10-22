"""
ORM、处理代码与SQL的映射关系
Django 还提供了原生SQL 的接口Post.objects.raw('SELECT* FROM blog_post ’ ），它除了可以
解决Query Set 无法满足查询的情况外，还可以提高执行效率。不过，我们需要严格把控使用场景，
因为过多地使用原生SQL 会提高维护成本。

QuerySets、处理对应的数据库操作
在Django 的Model中，QuerySet 是一个重要的概念，必须了解！ 因为我们同数据库的所
有查询以及更新交互都是通过它来完成的。

数据的重要性;
一个系统的根基就是数据，所有业务都是建立在这个根基之上的。如果从数据层开始
就出了问题（偏差），那么其他层的开发也不会得到好结果。
"""

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '分类'  # 配置展示名为文章
        # 重新定义表名.
        # db_table = 'user_info'

    def __str__(self):
        return self.name

class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name="名称")
    # 对于有choices的字段，在admin后台， Django会提供一个下拉列表让用户选择，而不是填写，这对于用户来说非常友好。
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '标签'
        ordering = ['-id']

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField(max_length=255, verbose_name="标题")
    desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="正文", help_text="正文必须为MarkDown格式")
    content_html = models.TextField(verbose_name="正文html代码", blank=True, editable=False)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    is_md = models.BooleanField(default=False, verbose_name="markdown语法")
    # 创建一个外键、此处没有做好数据表关系设计(理解)
    category = models.ForeignKey(Category, verbose_name="分类", on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  # verbose_name 字段对应的展示文案

    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ['-id']

    def __str__(self):
        return self.title

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL) \
                .select_related('owner', 'category')
        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            post_list = []
        else:
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL) \
                .select_related('owner', 'category')
        return post_list, category

    @classmethod
    def latest_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL)


