from django.shortcuts import render
from django.http import HttpResponse
# Импортируем загрузчик.
from django.shortcuts import render

# Create your views here.
# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': 'Последние обновления на сайте'
    }
    return render(request, template, context)


# Страница с постами
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    poem = ('Вчера Крокодил<br>улыбнулся так злобно,<br>Что мне до сих'
            ' пор<br>за него неудобно.<br> Всем хорошего настроения :)<br>')
    context = {
        'title': title,
        'text': 'Лев Толстой – зеркало русской революции.',
        'poem': poem
    }
    return render(request, template, context)
