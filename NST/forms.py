from django import forms

CHOICES = (('Wassily_Kandinsky.jpg', 'Wassily Kandinsky'),)  # temporary placeholder


class NSTForm(forms.Form):
    image_input = forms.ImageField(label='Select an image you want to transform')
    style_select = forms.ChoiceField(label='Select a desired style of the new image',
                                     choices=CHOICES, widget=forms.RadioSelect())
