import django_filters
from .models import EmployeeDB 

class Employeefilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')

    class Meta:
        model  = EmployeeDB
        fields = {
            'OSID' : ['icontains'],
            'first_name' : ['icontains'],
            'BL' : ['icontains'],
            'grade' : ['icontains'],
        }


    def filter_by_order(self,queryset, name, value):
        expression  = 'first_name' if value == 'ascending' else  '-description'
        return queryset.order_by(expression)
