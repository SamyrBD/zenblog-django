# blog/urls.py
from django.urls import path
from . import views
from .views import (
    ArticleListView, 
    ArticleDetailView, 
    ArticleCreateView,
    CategoryCreateView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('contact/', views.contact_view, name='contact'),
    
    # --- RUTAS NUEVAS PARA CREAR ---
    path('article/new/', ArticleCreateView.as_view(), name='article_create'),
    path('category/new/', CategoryCreateView.as_view(), name='category_create'),
]