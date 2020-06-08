from django.shortcuts import render


def index(request):
    return render(request, 'NST/index.html')
