from django.contrib import admin
from .models import Category, Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'publication_date')
    list_filter = ('category', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)