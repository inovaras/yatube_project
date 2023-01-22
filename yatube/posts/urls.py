# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страницы с отфильтрованными по группам постами
    path('group/<slug:slug>/', views.group_posts),
]
