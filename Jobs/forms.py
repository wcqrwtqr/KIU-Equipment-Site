from .models import JobsDB
from django import forms

class JobsForm(forms.ModelForm):
    class Meta:
        model = JobsDB
        fields = '__all__'

        bu = [('KIU','KIU'),('SIU','SIU'), ('AGU','AGU'), ('NAU','NAU'), ('ADU','ADU'),]
        bl = [('SWT','SWT'),('SLS','SLS'), ('WHM','WHM'), ('DST','DST'),]

        widgets  = {
            'description' : forms.Textarea(attrs={'rows':3 }),
            'startDate' : forms.SelectDateWidget(years=[x for x in range(2013,2025)]),
            'endDate' : forms.SelectDateWidget(years=[x for x in range(2013,2025)]),
            'BU' : forms.Select(choices=bu),
            'BL' : forms.Select(choices=bl),
        }




