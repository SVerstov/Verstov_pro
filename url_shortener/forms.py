from django import forms
from .models import ShortenerFields
from django.core.exceptions import ValidationError
import re


class ShortenerForm(forms.ModelForm):
    class Meta:
        model = ShortenerFields
        fields = '__all__'
