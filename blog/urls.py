from django.urls import path
from blog.views import *

urlpatterns = [
    path('', blog_view,name='blog'),
    path('single', blog_single_view, name='single'),
    path('post-<int:pid>', test, name='test'),


]