from django.shortcuts import render
from blog.models import Post
# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(status = True)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request):
    context = {'title': 'bitcoin crashed', 'content': 'bitcoin was flying but now grounded!', 'author': 'alireza farshi'}
    return render(request, 'blog/blog-single.html', context)

def test(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'test.html', context)

