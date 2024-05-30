from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article


# Create your views here.


# def home(request):
#     return HttpResponse('Hello world. My name is fahimeh.')
#
#
# def api(request):
#     data = {
#         '1': {'tite': 'first article', 'slog': 1},
#         '2': {'tite': 'second article', 'slog': 2},
#         '3': {'tite': 'third article', 'slog': 3},
#     }
#     return JsonResponse(data)
# def home_1(request):
#     context = {
#         "articles": [
#             {'title': 'تصاویر و مشخصات لپ‌تاپ‌های آینده دل و لنوو با پردازنده اسنپدراگون X فاش شد',
#              'image': 'https://static.digiato.com/digiato/2024/05/Dell-Snapdragon-X-910x600.jpg'},
#             {'title': 'بریتانیا برای تقویت ایمنی مدل‌های هوش مصنوعی یک نرم‌افزار جدید معرفی کرد',
#              'image': 'https://static.digiato.com/digiato/2024/05/index-1-910x600.jpeg'},
#             {'title': 'گوگل سری پیکسل 8 را با درنظرگرفتن استفاده از قاب محافظ طراحی کرده است',
#              'image': 'https://static.digiato.com/digiato/2024/05/google-pixel-8-offical-cases-910x600.jpg'},
#         ]
#     }
#     return render(request, template_name='blog.html', context=context)


def home_2(request):
    context = {'articles': Article.objects.filter(status='p').order_by('-publish')}
    # return render(request, template_name='blog.html', context=context)
    return render(request, template_name='blog/index.html', context=context)


def detail_article(request, slug):
    context = {
        'article': Article.objects.get(slug=slug)
    }
    return render(request, template_name='detail.html', context=context)
