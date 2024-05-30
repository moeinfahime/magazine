from django.contrib import admin
from .models import Article


# Register your models here.
class AdminModel(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']


admin.site.register(Article, AdminModel)