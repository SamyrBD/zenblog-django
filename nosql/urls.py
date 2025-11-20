from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_article_view, name='nosql_list'),
    path('nuevo/', views.create_article_view, name='nosql_create'),
    path('nueva-categoria/', views.create_category_view, name='nosql_category_create'),
    path('article/<str:doc_id>/', views.detail_view, name='nosql_detail'),
]