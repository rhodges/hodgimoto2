from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path(r'page/(?P<id>\d+)/$', views.post_page, name='post_page'),
]
