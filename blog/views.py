from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.utils import timezone
# Create your views here.


def blog_view(request, cat_name=None):
    current_time = timezone.now()
    posts = Post.objects.filter(status=True)
    posts = posts.exclude(published_date__gt=current_time)
    if cat_name:
        posts = posts.filter(category__name=cat_name)

    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    posts = Post.objects.filter(status=True)
    post = get_object_or_404(posts, pk=pid)
    post.counted_views += 1
    post.save()
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)


def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'test.html', context)


def test2(request):
    return render(request, 'test.html')


