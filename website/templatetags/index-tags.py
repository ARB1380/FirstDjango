from django import template
from blog.models import Post
from django.utils import timezone


register = template.Library()


@register.inclusion_tag('website/latest-posts.html')
def show_latest_posts():
    current_time = timezone.now()
    posts = Post.objects.filter(status=1)
    posts = posts.exclude(published_date__gt=current_time)
    posts = posts.order_by('published_date')[:6]
    print(len(posts))
    return {'posts': posts}