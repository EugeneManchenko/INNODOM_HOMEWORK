from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['somer', 'hello', '123']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
