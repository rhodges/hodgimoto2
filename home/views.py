from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.
def home(request):
    latest_blog_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[0:3]
    return render(request, 'home/home.html', {'latest_blog_posts': latest_blog_posts})
