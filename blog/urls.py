# from .views import home, api
# from .views import home_1
from .views import home_2, detail_article
from django.urls import path

name_app = "blog"
urlpatterns = [
    # path('', home_1, name='home_1'),
    path('', home_2, name='home_2'),
    # path('api', api, name='api'),
    path('article/detail/<slug:slug>', detail_article, name='detail')
]
