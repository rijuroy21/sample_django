from django import forms
from .models import *

class model_form(forms.ModelForm):
    class Meta:
        model=teacher
        fields='__all__'