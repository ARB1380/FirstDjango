from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.published_date

    def location(self, item):
        return reverse('single', kwargs={'pid': item.id})