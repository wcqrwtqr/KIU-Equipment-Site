from .models import EmployeeDB
from django import forms

class EmployeeFormNew(forms.ModelForm):
    class Meta:
        model = EmployeeDB
        fields = '__all__'

