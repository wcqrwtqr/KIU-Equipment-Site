from .models import FAR_DB
from django import forms

class FarForm(forms.ModelForm):
    class Meta:
        model = FAR_DB
        fields = '__all__'


