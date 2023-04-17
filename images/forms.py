from django import forms
from django.forms import modelformset_factory
from.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']


ImageFormSet = modelformset_factory(Image, form=ImageForm, max_num=5, extra=5)

