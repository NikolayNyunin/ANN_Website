# import os

from django.shortcuts import render

from .forms import NSTForm


def home(request):
    form = NSTForm(request.POST)

    # style_dir_path = 'NST/static/NST/images/styles'  # not sure if it is going to work in production
    #
    # style_images = [file for file in os.listdir(style_dir_path)]

    return render(request, 'NST/home.html', {'form': form})
