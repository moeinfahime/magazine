from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=10, unique=True, verbose_name='آدرس')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(null=True, verbose_name='پوزیشن')

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICE = [
        ('p', 'منتشر شده'),
        ('d', 'انتشار نیافته')
    ]
    title = models.CharField(max_length=20, verbose_name='عنوان')
    slug = models.SlugField(max_length=10, unique=True, verbose_name='آدرس مقاله')
    category = models.ManyToManyField(Category, verbose_name=' دسته بندی')
    description = models.TextField(verbose_name='توضیحات')
    thumbnail = models.ImageField(upload_to='Image', verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, verbose_name='وضعیت')

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return self.title
