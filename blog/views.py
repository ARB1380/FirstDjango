from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404
# Create your views here.


def blog_view(request):
    posts = Post.objects.filter(status = True)
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)


def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'test.html', context)

