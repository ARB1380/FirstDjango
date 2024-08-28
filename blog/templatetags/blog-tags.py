from django import template
from blog.models import Post
register = template.Library()


@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status= 1)
    return posts


@register.filter
def snippet(value, arg=20):
    return value[:arg] + '...'


@register.inclusion_tag('popular-posts.html')
def popular_posts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:1]
    return {'posts': posts}
