from .models import FAR_DB
from django import forms

class FarForm(forms.ModelForm):
    class Meta:
        model = FAR_DB
        fields = ('asset_num', 'serial_num', 'description', 'BU', 'BL' , 'asset_life', 'acquisition_cost', 'tot_dep_value', 'nbv', 'acquisition_date', 'equ_type', 'temp_location')


