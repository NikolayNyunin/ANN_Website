import os

from django import forms


def get_choices():
    style_dir = 'NST/static/NST/images/styles'
    style_images = [file for file in os.listdir(style_dir)]
    choices = [[image_name, ' '.join((' '.join(image_name.split('.')[:-1])).split('_'))] for image_name in style_images]
    return choices


class NSTForm(forms.Form):
    image_input = forms.ImageField(label='Select an image you want to transform')
    style_select = forms.ChoiceField(label='Select a desired style of the new image',
                                     choices=get_choices(), widget=forms.RadioSelect())
