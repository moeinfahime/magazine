from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    STATUS_CHOICE = [
        ('p', 'published'),
        ('d', 'draft')
    ]
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=10, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='Image')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE)

    def __str__(self):
        return self.title
