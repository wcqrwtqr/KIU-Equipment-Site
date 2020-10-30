from .models import EmployeeDB
from django import forms

class EmployeeFormNew(forms.ModelForm):
    class Meta:
        model = EmployeeDB
        fields = '__all__'

        bu = [('KIU','KIU'),('SIU','SIU'), ('AGU','AGU'), ('NAU','NAU'), ('ADU','ADU'),]
        bl = [('SWT','SWT'),('SLS','SLS'), ('WHM','WHM'), ('DST','DST'),]
        rotation = [('5x5','5x5'),('4x2','4x2'), ('6x3','6x3'), ('8x2','8x2'),]
        grade_level = [tuple([x,x]) for x in range(1,13)]
        widgets  = {
            'description' : forms.Textarea(attrs={'rows':3 }),
            'seniority_date' : forms.SelectDateWidget(years=[x for x in range(2009,2025)]),
            'BU' : forms.Select(choices=bu),
            'BL' : forms.Select(choices=bl),
            'rotation' : forms.Select(choices=rotation),
            'grade' : forms.Select(choices = grade_level ),
        }



