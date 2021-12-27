from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=25, null=True)
    content = models.TextField(max_length=500, null=True)
    review = models.TextField(max_length=2500, null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):      # this function returns url according to path in urls.py
        return reverse('post', kwargs={'post_slug': self.slug})


class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_content = models.TextField(max_length=2500, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.news_title
