from django import forms
from .models import MaintenanceDB


class MaintenanceForm (forms.ModelForm):
    class Meta:
       model = MaintenanceDB
       fields = '__all__' 
