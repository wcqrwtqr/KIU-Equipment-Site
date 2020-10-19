from .models import JobsDB
from django import forms

class JobsForm(forms.ModelForm):
    class Meta:
        model = JobsDB
        fields = '__all__'

