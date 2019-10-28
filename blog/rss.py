"""
提供一个RSS 和sitemap 输出的接口。RSS ( Really Simple Syndication ，简易信息聚合）
用来提供订阅接口，让网站用户可以通过RSS阅读器订阅我们的网站，在有更新时，RSS阅读
器会自动获取最新内容，网站用户可以在RSS 阅读器中看到最新的内容，从而避免每次都需
要打开网站才能看到是否有更新。
"""
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed


from .models import Post


class ExtendedRSSFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed, self).add_item_elements(handler, item)
        handler.addQuickElement('content:html', item['content_html'])


class LatestPostFeed(Feed):
    feed_type = ExtendedRSSFeed  # 其中feed_type 可以不写，默认使用Rss201rev2Feed
    title = "Bruce Blog System"
    link = "/rss/"
    description = "Bruce is a blog system power by django"

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.desc

    def item_link(self, item):
        return reverse('post-detail', args=[item.pk])

    def item_extra_kwargs(self, item):
        return {'content_html': self.item_content_html(item)}

    def item_content_html(self, item):
        return item.content_html
