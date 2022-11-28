from .models import Test
from django.forms import ModelForm
from django import forms


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['test_name','test_text']
