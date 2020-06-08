from django.shortcuts import render


def index(request):
    style_images = ['Wassily_Kandinsky.jpg']  # temporary placeholder
    return render(request, 'NST/index.html', {'style_images': style_images})
