from django import template
from blog.models import Post


register = template.Library()


@register.inclusion_tag('website/latest-posts.html')
def show_latest_posts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:6]
    print(len(posts))
    return {'posts': posts}