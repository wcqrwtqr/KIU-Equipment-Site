from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class MaintenanceList(TemplateView):
    template_name = 'Maintenance/maintenance_page.html'
