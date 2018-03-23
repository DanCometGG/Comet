from django.shortcuts import render


def base(request):
    context = {}
    return render(request, 'base.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)


def grid(request):
    context = {}
    return render(request, 'grid.html', context)


