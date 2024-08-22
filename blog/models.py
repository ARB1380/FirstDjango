from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    # tag
    # category
    # author
    # image
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

