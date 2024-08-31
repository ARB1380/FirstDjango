from django.urls import path
from blog.views import *

urlpatterns = [
    path('', blog_view,name='blog'),
    path('<int:pid>', blog_single_view, name='single'),
    # path('post-<int:pid>', test, name='test'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    path('test', test2, name='test')



]