from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_page(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'blog/post_page.html', {'post': post})
