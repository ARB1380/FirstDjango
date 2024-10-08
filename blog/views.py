from django.shortcuts import render,redirect
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from website.models import Contact
from django.http import HttpResponse
from website.forms import NameForm
from website.forms import ContactForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# Create your views here.


def blog_view(request, **kwargs):
    current_time = timezone.now()
    posts = Post.objects.filter(status=True)
    posts = posts.exclude(published_date__gt=current_time)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    paginator = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)

    except PageNotAnInteger:
        posts = paginator.get_page(1)

    except EmptyPage:
        print("entered")
        posts = paginator.get_page(1)


    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request, pid):
    current_time = timezone.now()
    posts = Post.objects.filter(status=True)
    posts = posts.exclude(published_date__gt=current_time)
    post = get_object_or_404(posts, pk=pid)
    if not post.login_require:
        post_index = list(posts).index(post)
        previous_post = posts[post_index - 1] if post_index > 0 else None
        next_post = posts[post_index + 1] if post_index < len(posts) - 1 else None
        post.counted_views += 1
        post.save()
        print(post.tags)
        context = {'post': post, 'previous_post': previous_post, 'next_post' : next_post}
        return render(request, 'blog/blog-single.html', context)

    else:
        return redirect(reverse('login'))


def blog_search(request):
    current_time = timezone.now()
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        print(request.GET.get('s'))

    posts = posts.exclude(published_date__gt=current_time)
    if s := request.GET.get('s'):
        posts = posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)



def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'test.html', context)


def test2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    form = ContactForm()

    return render(request, 'test.html', {'form' : form})


