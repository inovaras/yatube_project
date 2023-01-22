from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница с постами
def group_posts(request, slug):
    return HttpResponse(f'Вы открыли страницy, '
                        f'с отфильтрованными по группам {slug} постами.')
