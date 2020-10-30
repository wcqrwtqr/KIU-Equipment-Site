from .models import FAR_DB
from django import forms

class FarForm(forms.ModelForm):

    class Meta:
        bu = [('KIU','KIU'),('SIU','SIU'), ('AGU','AGU'), ('NAU','NAU'), ('ADU','ADU'),]
        bl = [('SWT','SWT'),('SLS','SLS'), ('WHM','WHM'), ('DST','DST'),]
        model = FAR_DB
        fields = '__all__'
        widgets  = {
            'description' : forms.Textarea(attrs={'rows':3 }),
            'acquisition_date' : forms.SelectDateWidget(years=[x for x in range(2009,2025)]),
            'BU' : forms.Select(choices=bu),
            'BL' : forms.Select(choices=bl),
        }


