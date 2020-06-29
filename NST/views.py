from django.shortcuts import render

from .forms import NSTForm
from .utils import nst


def home(request):
    if request.method == 'POST':
        form = NSTForm(request.POST, request.FILES)
        if form.is_valid():
            input_image, style_image_path = form.cleaned_data.get('image_input'), form.cleaned_data.get('style_select')

            output_image_url = nst(input_image, style_image_path)
            return render(request, 'NST/home.html', {'form': form, 'output_image_url': output_image_url})
        return render(request, 'NST/home.html', {'form': form})

    form = NSTForm()

    return render(request, 'NST/home.html', {'form': form})
