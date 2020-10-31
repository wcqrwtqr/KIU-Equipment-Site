import django_filters
from .models import FAR_DB

class FARfilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')

    class Meta:
        model  = FAR_DB
        fields = {
            'equ_type' : ['icontains'],
            'serial_num' : ['icontains'],
            'BU' : ['icontains'],
            'temp_location' : ['icontains'],
            'description' : ['icontains'],
            'BL' : ['icontains'],
        }

    def filter_by_order(self,queryset, name, value):
        expression  = 'description' if value == 'ascending' else  '-description'
        return queryset.order_by(expression)
