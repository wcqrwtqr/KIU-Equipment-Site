import django_filters
from .models import MaintenanceDB, FAR_DB

class Maintenancefilter(django_filters.FilterSet):
    CHOICES = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering  = django_filters.ChoiceFilter(label='Ordering', choices= CHOICES , method='filter_by_order')

    class Meta:
        model  = MaintenanceDB
        fields = ('asset','ms_type')
        # fields = {
        #     'ms_type' : ['icontains'],
        #     'asset' : ['contains'],
        # }

    def filter_by_order(self,queryset, name, value):
        expression  = 'description' if value == 'ascending' else  '-description'
        return queryset.order_by(expression)
