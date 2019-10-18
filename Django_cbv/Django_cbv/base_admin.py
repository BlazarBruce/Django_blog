"""
功能;抽取基类
说明：
1、一般抽取基类是完成代码的答题流程之后才做的、目的是为了方便维护
2、我们把这段代码放到base_admin.py 文件中，跟custom_site.py 同目录即可。之所以放这里，
是因为所有的App 都需要用到。
"""

from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1. 用来处理文章、分类、标签、侧边栏、友链这些model的owner字段自动补充
    2. 用来针对queryset过滤当前用户的数据
    """
    exclude = ('owner', )

    def get_queryset(self, request):

        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)



