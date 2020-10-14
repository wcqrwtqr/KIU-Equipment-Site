from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,View
from .models import MaintenanceDB
# Create your views here.

class MaintenanceHomePage(ListView):
    template_name = 'Maintenance/maintenance_page.html'
    queryset = MaintenanceDB.objects.all()
    context_object_name = 'main_all'

class MaintenanceDetailView(DetailView):
    template_name = 'Maintenance/maintenance_detail.html'
    queryset = MaintenanceDB.objects.all()
    context_object_name = 'maintenance_detail'
