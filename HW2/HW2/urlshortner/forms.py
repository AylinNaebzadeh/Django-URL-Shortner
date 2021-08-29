from django.db import models
from django.forms import ModelForm, fields
from .models import Url


class URLForm(ModelForm):
    class Meta:
        model = Url
        fields = ['link']
        labels = {
            'link' : 'Enter link'
        }