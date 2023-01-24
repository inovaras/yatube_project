# posts/urls.py
from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страницы с отфильтрованными по группам постами
    path('group/<slug:slug>/', views.group_posts),
    path('group/all_group_posts/', views.group_posts, name='all_group_posts'),
]
