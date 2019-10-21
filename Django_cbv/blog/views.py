from django.shortcuts import render
from django.http import HttpResponse

def post_list(request, category_id=None, tag_id=None):

    return render(request, 'blog/list.html', context={'name': 'post_list'})

def post_detail(request, post_id):

    return render(request, 'blog/detail.html', context={'name': 'post_detail'})
