from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response  # 渲染器

from .models import Post
from .serializers import PostSerializer

@api_view
def post_list(request):
    posts = Post.objects.filter(status=Post.STATUS_NORMAL)  # 从数据库中去除状态蒸菜的文章
    post_serializers = PostSerializer(posts, many=True)  # 对queryset进行序列化
    return Response(post_serializers.data)  # 返回序列化的数据、并用渲染器进行渲染

class PostList(generics.ListCreateAPIView):
    posts = Post.objects.filter(status=Post.STATUS_NORMAL)  # 从数据库中去除状态蒸菜的文章
    serializer_class = PostSerializer  # 配置自定义的序列化类

