from django import forms

from .models import Style


def get_choices():
    styles = Style.objects.all()
    choices = [(style.image.path, style.name) for style in styles]
    return choices


class NSTForm(forms.Form):
    image_input = forms.ImageField(label='Select an image you want to transform')
    style_select = forms.ChoiceField(label='Select a desired style of the new image',
                                     choices=get_choices(), widget=forms.RadioSelect())
